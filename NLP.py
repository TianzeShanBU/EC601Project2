import os
from google.cloud import language_v1

credential_path = "D:\Download\ec601-327201-544fe77b03a7.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

# Instantiates a client
client = language_v1.LanguageServiceClient()

# The text to analyze
text = "Boston is best known for its famous baked beans, Fenway Park, The Boston Marathon, and of course for the bar from Cheers, but dig a little deeper below the surface and you'll find a surprising wealth of things that make Boston one of the best cities in America—and the world."
document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment

print("Text: {}".format(text))
print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))

