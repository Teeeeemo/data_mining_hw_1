import nltk
from nltk.corpus import stopwords
import pandas as pd

"""
Helper functions for data mining lab session 2017 Fall
Notations:
d - document
D - documents
V - vowels
w - word
W - words
l - letter
"""

def format_rows(docs):
    """ format the text field and strip special characters """
    D = []
    for d in docs.data:
        temp_d = " ".join(d.split("\n")).strip('\n\t')
        D.append([temp_d])
    return D

def format_labels(target, docs):
    """ format the labels """
    return docs.target_names[target]

def check_missing_values(row):
    """ functions that check and verifies if there are missing values in dataframe """
    # Faster way to summarize if a series contains null values or not
    # [Ref] https://stackoverflow.com/a/29530601
    return ("The amoung of missing records is: ", pd.Series.sum(row))

def tokenize_text(text, remove_stopwords=False):
    """
    Tokenize text using the nltk library
    """
    stop_words = stopwords.words('english')
    tokens = []
    for d in nltk.sent_tokenize(text, language='english'):
        for word in nltk.word_tokenize(d, language='english'):
            if (word not in stop_words or not remove_stopwords):
                tokens.append(word)
    return tokens