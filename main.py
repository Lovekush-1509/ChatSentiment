import streamlit as st
import pandas as pd
import altair as alt
from chatBot import ChatBot 

# Initialize chatbot in session state
if "bot" not in st.session_state:
    st.session_state.bot = ChatBot()

bot = st.session_state.bot



st.title("Chat Sentiment Analyzer Bot")
st.write("Type your message and see sentiment analysis in real-time!")

# User input
user_input = st.text_input("You:")

if st.button("Send") and user_input.strip():
    # Use existing class methods
    sentiment = bot.analyzer.analyze(user_input)
    bot.conversation.append(user_input)
    bot.sentiments.append(sentiment)

    # Bot reply logic (from original class)
    if sentiment == "Negative":
        bot_reply = "I'll make sure your concern is addressed."
    elif sentiment == "Positive":
        bot_reply = "Thanks for sharing your feedback!"
    else:
        bot_reply = "Thanks for sharing."

    # Display
    st.markdown(f"**You:** {user_input}")
    st.markdown(f"**Sentiment:** {sentiment}")
    st.markdown(f"**Bot:** {bot_reply}")

# Show conversation history
if bot.conversation:
    st.subheader("Conversation History")
    df = pd.DataFrame({
        "Message": bot.conversation,
        "Sentiment": bot.sentiments
    })
    st.table(df)

# Generate summary & graph
if st.button("Generate Summary") and bot.conversation:
    complete_conversation = " ".join(bot.conversation)
    overall_sentiment = bot.analyzer.analyze(complete_conversation)
    satisfaction = bot.analyzer.polarityScore(complete_conversation)

    st.subheader("Conversation Summary")
    st.markdown(f"**Overall Sentiment:** {overall_sentiment}")
    st.markdown(f"**Satisfaction Level:** {satisfaction}")

    # Mood Trend Chart
    mood_counts = df['Sentiment'].value_counts().reset_index()
    mood_counts.columns = ["Sentiment", "Count"]

    chart = alt.Chart(mood_counts).mark_bar().encode(
        x='Sentiment',
        y='Count',
        color='Sentiment',
        tooltip=['Sentiment', 'Count']
    ).properties(title="Mood Trend")

    st.altair_chart(chart, use_container_width=True)
