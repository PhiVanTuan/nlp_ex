from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

data_set=open("vocab.txt").read().splitlines()
count_vectorizer = CountVectorizer(binary='true',vocabulary=data_set)
print(count_vectorizer)
# data = count_vectorizer.fit_transform(data_set)

data_negative=open("negative.txt").read()
data_positive=open("positive.txt")

#get dict word
def getWord(data_negative):
    numOfWordsA = dict.fromkeys(data_set, 0)
    for x in data_negative.splitlines():
        bagOfWordsA = x.split()
        for word in bagOfWordsA:
            numOfWordsA[word] += 1
    return numOfWordsA


for line in data_negative.splitlines():
    print(line)
    list=[]
    list.append(line)
    X=count_vectorizer.fit_transform(list)
    print(X.toarray())
#     np.array()
# word_negative=getWord(data_negative)


