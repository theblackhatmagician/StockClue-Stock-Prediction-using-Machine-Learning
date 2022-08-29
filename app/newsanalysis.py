import re
import pandas as pd
import numpy as np
import nltk
import string
from nltk.corpus import stopwords
stop = stopwords.words("english")
import datetime as dt
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer
english_stemmer=nltk.stem.SnowballStemmer('english')
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer


def cleaning( review, remove_stopwords=True):
    review_text = re.sub("[^a-zA-Z]"," ", review)
    words = review_text.lower().split()
    if remove_stopwords:
        stops = set(stopwords.words("english"))
        words = [w for w in words if not w in stops]
    b=[]
    stemmer = english_stemmer 
    for word in words:
        b.append(stemmer.stem(word))
    return(words)

def newsSenti(data):
    clean_Text = []
    for review in data:
        clean_Text.append( " ".join(cleaning(str(review[0]))))

    from nltk.sentiment.vader import SentimentIntensityAnalyzer

    Senti = SentimentIntensityAnalyzer()
    sample_review = clean_Text
    count = 0
    neg = 0
    pos = 0
    neu = 0
    for sentence in sample_review:
        ss = Senti.polarity_scores(sentence)
        count += 1
        neg += ss['neg']
        neu += ss['neu']
        pos += ss['pos']

    sentiment = []
    sentiment.append((neg/count)*100)
    sentiment.append((neu/count)*100)
    sentiment.append((pos/count)*100)

    return sentiment


