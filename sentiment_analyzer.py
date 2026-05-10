from textblob import TextBlob

def choose(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    if sentiment.polarity > 0:
        return "Happy", sentiment.polarity
    elif sentiment.polarity < 0:
        return "Sad", sentiment.polarity
    else:
        return "Neutral", sentiment.polarity

text = input("Enter your text: ")
mood , polarity = choose(text)

print(f"Your mood is: {mood} with a polarity of {polarity}")
