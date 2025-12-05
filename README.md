#  ChatSentimentBot

A **Python-based chatbot** that interacts with users and performs **sentiment analysis** to evaluate the overall emotional tone of the conversation.

---

##  Project Overview

**ChatSentimentBot** is designed to maintain the full conversation history while interacting with the user. At the end of the chat, it calculates the overall sentiment score, indicating whether the conversation mood is **Positive**, **Neutral**, or **Negative**.

Key highlights:  
- Modular design using `chatBot.py` for chatbot logic.  
- `main.py` initializes the chatbot and starts the conversation.  
- Performs sentiment analysis for the full conversation or optionally for each user message.  
- Provides interactive responses while tracking user sentiment in real-time.  

---



## ✨ Features & Functionalities

### 1. Conversation Management
- Maintains **full conversation history**.  
- Accepts messages until user types `"exit"`.  
- Stores messages and their corresponding sentiment.

### 2. Per-Message Sentiment Analysis
- Analyzes each user message for sentiment: **Positive, Negative, Neutral**.  
- Displays sentiment immediately after each user message.

### 3. Interactive Bot Responses
- Responds based on message sentiment:  
  - Negative → `"I'll make sure your concern is addressed."`  
  - Positive → `"Thanks for sharing your feedback!"`  
  - Neutral → `"Thanks for sharing."`  

### 4. Overall Conversation Analysis
- Combines all messages to calculate **overall sentiment**.  
- Computes **satisfaction level** using polarity scores.  
- Displays **final summary** with sentiment and satisfaction level.

### 5. Polarity & Satisfaction Scoring
- Polarity obtained from **TextBlob**.  
- Satisfaction score formula:  
```python```
satisfactionScore = int((polarity + 1) * 50)




## Technologies Used

- **Language:** Python 3.x  
- **Libraries:**  
  - `textblob` → Sentiment analysis and polarity calculation   
- **Structure:**  
  - `chatBot.py` → Handles chatbot logic and conversation flow  
  - `sentimental_analyzer.py` → Handles sentiment analysis and satisfaction scoring  
  - `main.py` → Entry point to start the chatbot  

    LIAPLUS/
    ├── main.py                  # Entry point to start the chatbot

    ├── chatBot.py               # Handles chatbot logic and conversation flow

    ├── sentimental_analyzer.py  # Handles sentiment analysis and satisfaction scoring

    ├── requirements.txt         # Python dependencies

    ├── README.md                # Project documentation
    
    └── tests/                   # Optional: Unit tests for chatbot and sentiment analysis



---

## Sentiment Analysis Logic

- The chatbot uses `TextBlob` to compute **polarity** for user messages.  
- **Sentiment labels:**  
  - `polarity > 0` → Positive  
  - `polarity < 0` → Negative  
  - `polarity = 0` → Neutral  

- **Satisfaction levels** are computed as:  
```python```
satisfactionScore = int((polarity + 1) * 50).


---


## ChatBot Module

`chatBot.py` is the core module of **ChatSentimentBot** that handles the **conversation flow**, **per-message sentiment analysis**, and generates the **overall sentiment summary** at the end of a chat session.

---

## Module Overview

The `ChatBot` class provides:  

- **Conversation management:** Stores all user messages in a conversation history.  
- **Per-message sentiment analysis:** Uses the `SentimentAnalyzer` class to determine if each user message is Positive, Negative, or Neutral.  
- **Interactive responses:** Automatically responds based on the sentiment of the user’s message.  
- **Overall conversation summary:** Generates the overall sentiment and satisfaction level when the user exits the chat.

---

