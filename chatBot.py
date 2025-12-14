from sentimentAnalyzer import SentimentAnalyzer

class ChatBot:

    # prepare the chatbot for conversation
    def __init__(self):
        self.conversation = []
        self.sentiments = []
        self.analyzer = SentimentAnalyzer()

    # starting chatbot for conversation with the user 
    # and analyzing the sentiment of the user's every statement
    def startChat(self):
        # exit condition 
        print("Chatbot started! (type 'exit' to stop)\n")

        # loop for the conversation until user type *exit*
        while True:
            user_msg = input("You: ")

            # Exit condition
            if user_msg.lower() == "exit":
                break

            # Analyze sentiment
            sentiment = self.analyzer.analyze(user_msg)

            # Storing sentiment and conversation for further analysis
            self.conversation.append(user_msg)
            self.sentiments.append(sentiment)

            # Display polarity of current user's statement
            print("→ Sentiment:",sentiment)

        
            if sentiment == "Negative":
                print("Bot: I'll make sure your concern is addressed.")
            elif sentiment == "Positive":
                print("Bot: Thanks for sharing your feedback!")
            else:
                print("Bot: Thanks for sharing.")

            print()

        # generating overall sentiment of the conversation
        self.generateSummary()

  
    def generateSummary(self):

        # Overall Sentiment
        completeConversation = " ".join(self.conversation)
        overallSentiment = self.analyzer.analyze(completeConversation)
        satisfactionLevel = self.analyzer.polarityScore(completeConversation)


         # Mood Trend (Bonus)
        positives = self.sentiments.count("Positive")
        negatives = self.sentiments.count("Negative")
        neutrals = self.sentiments.count("Neutral")

        print("\nMood Trend:")
        print(f"Positive: {positives}")
        print(f"Negative: {negatives}")
        print(f"Neutral : {neutrals}")


        print("\nFINAL OUTPUT:")
        print("Overall conversation sentiment:",overallSentiment,"-",satisfactionLevel)
        print("\n--------------------------------")
