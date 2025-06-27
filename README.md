# 📊 WhatsApp Chat Analyzer

This project is a **WhatsApp Chat Analyzer Web Application** built using Python and Streamlit. It allows users to upload exported WhatsApp chat files and receive detailed analytics and visualizations about the conversation, including message statistics, emoji usage, word clouds, and time-based activity.

---

## 🔗 Project Link

👉 [Live App on Streamlit](https://whatsapp-chat-analyzer-9vce8cezr6brwsvpbmxnwb.streamlit.app/)

---

## 🧠 Project Overview

WhatsApp is one of the most widely used messaging platforms. This project offers users an intuitive interface to upload and analyze their chat data. It extracts insights such as:

- Most active participants
- Message frequency over time
- Word usage and trends
- Emoji usage and distribution
- Busiest hours/days for messaging

The app transforms plain `.txt` chat data into engaging charts using **matplotlib**, **seaborn**, and **plotly**, offering clear, visual communication of conversation trends.

---

## 📂 Dataset

You can export any personal or group WhatsApp chat from the app itself:

1. Open a WhatsApp conversation
2. Tap the three-dot menu → **More** → **Export Chat**
3. Choose **Without Media**
4. A `.txt` file will be generated, which can be uploaded in the app

This file becomes the input for the analyzer.

---

## 🚀 Features

- 🔍 Extracts and cleans raw WhatsApp chat data
- 👤 Identifies most active users
- 📅 Analyzes messages by day, month, and hour
- ⏰ Highlights busiest time periods
- 🔤 Generates a word cloud from most frequently used words
- 😂 Analyzes emoji usage and displays a pie chart with emojis as labels
- 📈 Presents visual insights using bar, line, pie, and scatter charts

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| **Python** | Core programming language |
| **Pandas** | Data manipulation and analysis |
| **Matplotlib** | Plotting graphs |
| **Seaborn** | Statistical visualization |
| **Plotly** | Interactive plots |
| **Streamlit** | Front-end web interface |
| **Regular Expressions (re)** | Chat text cleaning and parsing |

---

## 📦 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/HemaGarima/WhatsApp-Chat-Analyzer.git
   cd WhatsApp-Chat-Analyzer

2. **Install required libraries:**

   ```bash
    python -m venv venv
    source venv/bin/activate  # or venv\Scripts\activate on Windows

3. **Run the app**

   ```bash
   streamlit run app.py
