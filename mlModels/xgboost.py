import regex as re
import pickle
import xgboost
import numpy as np

def clean_text(text):
        text = re.sub(r"\b\?s", "'s", text)
        text = re.sub(r"\\+", "", text)
        text = re.sub(r"\"", "", text)
        text = re.sub(r"\'?(\[|\])\'?", "", text)
        return text


def xgboost(news,series):
    news_list = [news[0][1],news[1][1],news[2[0]]]

    compound_scores = []
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    analyser = SentimentIntensityAnalyzer()
    import pandas as pd
    for news in news_list:
        cleaned_news = clean_text(news)
        comp = analyser.polarity_scores(cleaned_news)
        compound_scores.append(comp)

    x_input  = []
    x_input.append([series[0]['open'],series[1]['open'],series[2]['open']])
    x_input.append([series[0]['close'],series[1]['close'],series[2]['close']])
    x_input.append([series[0]['volume'],series[1]['volume'],series[2]['volume']])
    x_input.append(compound_scores)

    model = pickle.load(open(r"C:\Users\prana\Desktop\stockclue\mlModels\xgb_model.dat", "rb"))
    scaled_x = np.array(x_input)

    prediction = model.predict(scaled_x)
    return prediction
