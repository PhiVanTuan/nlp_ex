from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import numpy as np
import nltk

data=open("sentiment.txt")
stopWords = set(stopwords.words('english'))

def remove_stop_words(data):

    words = word_tokenize(str(data))
    new_text = ""
    for w in words:
        if not checkStopword(w) and len(w) > 1:
            new_text = new_text + " " + w
    return new_text

def stemming(data):
    stemmer = PorterStemmer()
    tokens = word_tokenize(str(data))
    new_text = ""
    for w in tokens:
        new_text = new_text + " " + stemmer.stem(w)
    return new_text

def checkStopword(str):
    if str in stopWords:return True
    else:return False

def preprocess(data):
    data = remove_stop_words(data)
    data = stemming(data)
    data = remove_stop_words(data)
    return data
processed_text = []
for i in data:
    processed_text.append(word_tokenize(preprocess(i)))
print(processed_text)
processed_text