from sentimentAnalyzer import SentimentAnalyzer


testCases = [
    # Positive
    ("I love this product", "Positive"),
    ("Amazing work!", "Positive"),
    ("This is fantastic", "Positive"),
    ("I'm very happy with the service", "Positive"),
    ("Excellent experience", "Positive"),
    ("I am satisfied", "Positive"),
    ("Great job", "Positive"),
    ("I enjoyed this", "Positive"),
    ("Wonderful product", "Positive"),
    ("Highly recommend this", "Positive"),
    ("I am thrilled with this", "Positive"),
    ("Absolutely fantastic!", "Positive"),
    ("I am delighted", "Positive"),
    ("Superb service", "Positive"),
    ("Totally satisfied", "Positive"),
    ("Everything is perfect", "Positive"),
    ("I feel okay about this", "Positive"),
    ("It's good", "Positive"),
    
    # Negative
    ("This is terrible", "Negative"),
    ("Not satisfied at all", "Negative"),
    ("Very bad experience", "Negative"),
    ("I hate this", "Negative"),
    ("Disappointing service", "Negative"),
    ("Poor quality", "Negative"),
    ("I am unhappy with this", "Negative"),
    ("Awful product", "Negative"),
    ("Terrible job", "Negative"),
    ("I am very disappointed", "Negative"),
    ("Worst experience ever", "Negative"),
    ("Completely useless", "Negative"),
    ("Very poor service", "Negative"),
    ("Average service", "Negative"),
    ("not good", "Negative"),
    ("It is average", "Negative"),
    
    # Neutral
    ("This is a product", "Neutral"),
    ("It is what it is", "Neutral"),
    ("This works", "Neutral"),
    ("I don't mind it", "Neutral"),
    ("Standard experience", "Neutral"),
    ("This is acceptable", "Neutral"),
    ("I feel indifferent about it", "Neutral"),
    ("It meets the requirements", "Neutral")
]

testCases = testCases * 2
testCases = testCases[:100]


def implementedTests():
    sa = SentimentAnalyzer()
    for text, valid_levels in testCases:
        assert sa.analyze(text) == valid_levels



if __name__ == "__main__":
    implementedTests()
    print("-------------------All Tests Passed----------------")