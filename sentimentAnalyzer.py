from textblob import TextBlob


# SentimentAnalyzer class for checking the sentiment of a text
class SentimentAnalyzer:

    def analyze(self, text):
        polarity = TextBlob(text).sentiment.polarity

        if polarity > 0:
            return "Positive"
        elif polarity < 0:
            return "Negative"
        else:
            return "Neutral"



    def polarityScore(self,text):

        # calculating the satisfaction percentage based on the polarity
        polarity = TextBlob(text).sentiment.polarity
        satisfactionScore = int((float(polarity) + 1) * 50)
        # print("polarity:",satisfactionScore,"type:",type(satisfactionScore))
        
        # returning the satisfaction level based on the percentage
        if satisfactionScore >= 90:
            return "Outstanding"
        elif satisfactionScore >= 80:
            return "Excellent"
        elif satisfactionScore >= 55:
            return "Good"
        elif satisfactionScore >= 45:
            return "Fair"
        elif satisfactionScore >= 30:
            return "Needs Improvement"
        elif satisfactionScore >= 15:
            return "Poor"
        else:
            return "Unacceptable"