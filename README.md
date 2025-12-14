#  ChatSentimentBot

A **Python-based chatbot** that interacts with users and performs **sentiment analysis** to evaluate the overall emotional tone of the conversation.

---

## Live Demo

Check out the live app here: [ChatSentiment Live](https://chatsentiment-xprxstp34atxs2pc8rh2z9.streamlit.app/)

##  Project Overview

**ChatSentimentBot** is designed to maintain the full conversation history while interacting with the user. At the end of the chat, it calculates the overall sentiment score, indicating whether the conversation mood is **Positive**, **Neutral**, or **Negative**.

Key highlights:  
- Modular design using `chatBot.py` for chatbot logic.  
- `main.py` initializes the chatbot and starts the conversation.  
- Performs sentiment analysis for the full conversation or optionally for each user message.  
- Provides interactive responses while tracking user sentiment in real-time.  

---



## How to Run

### Step 1 — Clone the Repository

```
    git clone https://github.com/Lovekush-1509/ChatSentiment.git
```
```
    cd LIAPLUS 
```

---

### Step 2 — Install Dependencies

```
    pip install textblob
```

---

### Step 3 — Run the Bot

```
    python main.py
```

---

### Step 4 — Use the Chatbot

Type messages normally.  
Type "exit" to end the conversation and view the final sentiment summary.

---





## Technologies Used

### Technologies Used

- **Python 3** – Core programming language for chatbot logic and sentiment analysis.
- **TextBlob** – Python library for natural language processing, used for sentiment analysis and polarity scoring.
- **Automated Testing** – Python scripts with assertion-based testing for validating sentiment analysis outputs.
- **Command-line Interface (CLI)** – User interacts with the chatbot via the terminal. 
- **Structure:**  
  - `chatBot.py` → Handles chatbot logic and conversation flow  
  - `sentimental_analyzer.py` → Handles sentiment analysis and satisfaction scoring  
  - `main.py` → Entry point to start the chatbot  

    ```
        ## Project Structure

        LIAPLUS/
        ├── main.py                  # Entry point to start the chatbot
        ├── chatBot.py               # Handles chatbot logic and conversation flow
        ├── sentimental_analyzer.py  # Handles sentiment analysis and satisfaction scoring
        ├── requirements.txt         # Python dependencies
        ├── README.md                # Project documentation
        └── tests/                   # Optional: Unit tests for chatbot and sentiment analysis

    ```




---

## Sentiment Analysis Logic

- The chatbot uses `TextBlob` to compute **polarity** for user messages.  
- **Sentiment labels:**  
  - `polarity > 0` → Positive  
  - `polarity < 0` → Negative  
  - `polarity = 0` → Neutral  

- **Satisfaction levels** are computed as:  
```python```
```

    satisfactionScore = int((polarity + 1) * 50).
    
```

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


## Tier 2 Implementation Status
```

    Fully Implemented

```

- Per-message sentiment analysis is performed for every user input.
- Each user message is displayed with its sentiment label (Positive, Negative, Neutral).
- A Mood Trend Summary is generated at the end of the conversation showing:
  - Total number of Positive messages
  - Total number of Negative messages
  - Total number of Neutral messages


---


### Tests if Implemented Status
Automated tests have been created to verify the correctness of the sentiment analysis module.

Key Features:
- Dynamic Test Cases: 50+ unique sentences covering Positive, Negative, and Neutral sentiments; repeated to reach 100 tests.
- Automated Validation: Each message is passed through SentimentAnalyzer.analyze() and compared with the expected sentiment.
- Assertion-based Testing: Any mismatch raises an AssertionError, alerting the developer immediately.
- Run Tests Easily:
  Execute the test script using:
  python sentimentTest.py
  If all tests pass, the script prints:

  ```

  -------------------All Tests Passed----------------

  ```

---


### Highlights of Innovations, Additional Features, and Enhancements
- **Mood Trend Summary:** At the end of the conversation, the chatbot counts the number of Positive, Negative, and Neutral messages to show the overall mood trend.
- **Satisfaction Scoring:** Each conversation is assigned a satisfaction level (Outstanding, Excellent, Good, Fair, Needs Improvement, Poor, Unacceptable) based on the overall sentiment.
- **Statement-level Sentiment Analysis:** Every user message is analyzed individually, giving immediate feedback on sentiment.
- **Automated Testing:** Dynamic automated tests verify the correctness of sentiment analysis for 100 diverse messages.
- **Extensible Design:** Modular structure allows easy addition of new features, such as more advanced NLP analysis or custom responses.
- **User-friendly Interaction:** Chatbot provides empathetic responses based on the sentiment of the user’s message.
- **Scalable and Reusable:** The sentiment analyzer can be reused in other applications or integrated with other chatbot systems.



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