# Updated app.py
import streamlit as st
import preprocessor, helper
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = 'Segoe UI Emoji'

st.sidebar.title("Whatsapp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)

    
    user_list = df['user'].unique().tolist()
    if 'group_notification' in user_list:
        user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0, "Overall")

    selected_user = st.sidebar.selectbox("Show analysis wrt", user_list)

    if st.sidebar.button("Show Analysis"):

        num_messages, words, num_media_messages, num_links = helper.fetch_stats(selected_user, df)

        st.title("Top Statistics")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total Words")
            st.title(words)
        with col3:
            st.header("Media Shared")
            st.title(num_media_messages)
        with col4:
            st.header("Links Shared")
            st.title(num_links)

        st.title("Monthly Timeline")

        timeline = helper.monthly_timeline(selected_user, df)
        
        if not timeline.empty:
            fig, ax = plt.subplots()
            ax.plot(timeline['time'], timeline['message'], color='green')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
        else:
            st.warning("No data available to display the monthly timeline.")


        st.title("Daily Timeline")
        daily_timeline = helper.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='black')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        st.title('Activity Map')
        col1, col2 = st.columns(2)

        with col1:
            st.header("Most busy day")
            busy_day = helper.week_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_day.index, busy_day.values, color='purple')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        with col2:
            st.header("Most busy month")
            busy_month = helper.month_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values, color='orange')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        st.title("Weekly Activity Map")
        user_heatmap = helper.activity_heatmap(selected_user, df)
        if not user_heatmap.empty:
            fig, ax = plt.subplots()
            sns.heatmap(user_heatmap, ax=ax)
            st.pyplot(fig)
        else:
            st.warning("Not enough data to display the heatmap.")

        if selected_user == 'Overall':
            st.title('Most Busy Users')
            x, new_df = helper.most_busy_users(df)
            fig, ax = plt.subplots()
            col1, col2 = st.columns(2)

            with col1:
                ax.bar(x.index, x.values, color='red')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
            with col2:
                st.dataframe(new_df)

        st.title("Wordcloud")
        df_wc = helper.create_wordcloud(selected_user, df)
        if df_wc:
            fig, ax = plt.subplots()
            ax.imshow(df_wc)
            ax.axis("off")
            st.pyplot(fig)
        else:
            st.warning("Not enough textual data to generate WordCloud.")

        most_common_df = helper.most_common_words(selected_user, df)
        fig, ax = plt.subplots()
        ax.barh(most_common_df[0], most_common_df[1])
        plt.xticks(rotation='vertical')
        st.title('Most Common Words')
        st.pyplot(fig)

        emoji_df = helper.emoji_helper(selected_user, df)
        st.title("Emoji Analysis")
        col1, col2 = st.columns(2)
        with col1:
            st.dataframe(emoji_df)
        with col2:
            if not emoji_df.empty:

                # Prepare top emojis + "Others"
                top_emojis = emoji_df.head(4)
                other_sum = emoji_df[1][4:].sum()

                labels = top_emojis[0].tolist() + ['Others']
                counts = top_emojis[1].tolist() + [other_sum]
                total = sum(counts)

                # Create labels with emojis + percentage
                pie_labels = [f"{emoji} ({(count / total) * 100:.1f}%)" if emoji != 'Others' else f"Others ({(count / total) * 100:.1f}%)"
                            for emoji, count in zip(labels, counts)]

                # Plotting Pie Chart
                fig, ax = plt.subplots(figsize=(8, 6))
                wedges, texts = ax.pie(counts, labels=pie_labels, 
                                    colors=['#f94144', '#f3722c', '#90be6d', '#577590', '#d3d3d3'],
                                    startangle=140, wedgeprops=dict(width=0.4), 
                                    textprops=dict(fontsize=12))

                # Title and layout
                ax.set_title("Top Emoji Usage with Percentage", fontsize=16, fontweight='bold')
                plt.tight_layout()

                # Show in Streamlit
                st.pyplot(fig)

            else:
                st.warning("No emojis found in selected chat.")
