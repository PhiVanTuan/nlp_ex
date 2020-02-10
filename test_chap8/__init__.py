from collections import Counter
from os.path import isfile

import nltk
import num2words as num2words
import os
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import numpy as np

def readText(pathFile):
    file=open(pathFile)
    text=file.read()
    file.close()
    return text

def remove_stop_words(data):
    stop_words = stopwords.words('english')
    words = word_tokenize(str(data))
    new_text = ""
    for w in words:
        if w not in stop_words and len(w) > 1:
            new_text = new_text + " " + w
    return new_text

def remove_punctuation(data):
    symbols = "!\"#$%&()*+-./:;<=>?@[\]^_`{|}~\n"
    for i in range(len(symbols)):
        data = np.char.replace(data, symbols[i], ' ')
        data = np.char.replace(data, "  ", " ")
    data = np.char.replace(data, ',', '')
    return data


def stemming(data):
    stemmer = PorterStemmer()
    tokens = word_tokenize(str(data))
    new_text = ""
    for w in tokens:
        new_text = new_text + " " + stemmer.stem(w)
    return new_text

def clean_doc(pathFile):
    data=readText(pathFile)
    data=remove_punctuation(data)
    data=getAlpha(data)
    # data=remove_stop_words(data)
    # data=convert_numbers(data)
    # data = stemming(data)
    # data = remove_punctuation(data)
    # data = remove_stop_words(data)
    data=word_tokenize(str(data))
    # print(data)
    return data

def getAlpha(data):
    tokens = word_tokenize(str(data))
    new_text = ""
    for word in tokens:
        if word.isalpha():new_text+=word+" "
    return new_text
# filename = 'neg/cv000_29416.txt'
# clean_doc(filename)
# split into tokens by white space

def processText(data,vocab):
    vocab.update(data)
def readFile():
    for f in os.listdir("neg"):
       clean_doc("neg/"+f)

readFile()