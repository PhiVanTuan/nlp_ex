import string
from collections import Counter
from os.path import isfile

import nltk
import num2words as num2words
import os
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import numpy as np

vocab = Counter()


def readText(pathFile):
    file = open(pathFile, encoding='latin-1')
    text = file.read()
    file.close()
    return text


def remove_stop_words(data):
    stop_words = stopwords.words('english')
    data = [w for w in data if not w in stop_words]
    return data


def remove_punctuation(data):
    translator = str.maketrans('', '', string.punctuation)
    tokens = [w.translate(translator) for w in data]
    return tokens


def stemming(data):
    stemmer = PorterStemmer()
    data = [stemmer.stem(w) for w in data]
    return data


def clean_doc(data):
    data = data.split()
    data = remove_punctuation(data)
    data = getAlpha(data)
    data = remove_stop_words(data)
    data = stemming(data)
    data = remove_punctuation(data)
    data = remove_stop_words(data)
    print(data)
    return data


def getAlpha(data):
    tokens = [word for word in data if word.isalpha()]
    return tokens


def processText(pathFle, vocab):
    data = readText(pathFle)
    data = data.splitlines()
    for x in data:
        line = clean_doc(x)
        vocab.update(line)


def save_list(lines, filename):
    data = '\n'.join(lines)
    file = open(filename, 'w')
    file.write(data)
    file.close()


# processText("rt-polarity.neg", vocab)
# processText("rt-polarity.pos", vocab)
# min_occurane = 5
# tokens = [k for k, c in vocab.items() if c >= min_occurane]
# print(len(tokens))
# # save tokens to a vocabulary file
# save_list(tokens, 'vocab.txt')


# load vocabulary
vocab_filename = 'vocab.txt'
vocab = open(vocab_filename).read()
vocab = vocab.split()
vocab = set(vocab)


def writeReview(pathFile):
    lines = list()
    data = readText(pathFile)
    data = data.splitlines()
    for x in data:
        line = clean_doc(x)
        line = [w for w in line if w in vocab]
        line = " ".join(line)
        print(line)
        lines.append(line)
    return lines

# prepare negative reviews
# negative_lines = writeReview('rt-polarity.neg')
# data = '\n'.join(negative_lines)
# file = open("negative.txt", 'w')
# file.write(data)
# file.close()
# save_list(negative_lines, 'negative.txt')
# prepare positive reviews
# positive_lines = writeReview('rt-polarity.pos');
# data = '\n'.join(positive_lines)
# file = open("positive.txt", 'w')
# file.write(data)
# file.close()
