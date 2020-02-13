from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

import numpy as np
import pandas as pd
from sklearn.model_selection import GridSearchCV

data_set=open("vocab.txt").read().splitlines()
count_vectorizer = CountVectorizer()
tfidf_vector=TfidfVectorizer()
#
# # use counts from count vectorizer results to compute tf-idf values
# print(tfidf_vector)
# data = count_vectorizer.fit_transform(data_set)

data_negative=open("negative.txt").read()
data_positive=open("positive.txt").read()

#get dict word
def getWord(data_negative):
    numOfWordsA = dict.fromkeys(data_set, 0)
    for x in data_negative.splitlines():
        bagOfWordsA = x.split()
        for word in bagOfWordsA:
            numOfWordsA[word] += 1
    return numOfWordsA

# array_negative=count_vectorizer.fit_transform(data_negative.splitlines())
# array_positive=count_vectorizer.fit_transform(data_positive.splitlines())
# tfidf_negative = tfidf_vector.fit_transform(data_negative.splitlines())
# tfidf_positive = tfidf_vector.fit_transform(data_positive.splitlines())

# print(tfidf_negative)

data=open("test.txt").read().splitlines()

tf_idf=tfidf_vector.fit_transform(data)
print(tfidf_vector.get_feature_names())

array_train=[]
list=[]
for i in data_negative.splitlines():
    array_train.append(0)
for i in data_positive.splitlines():
    array_train.append(1)

print(tf_idf.toarray())
# X = count_vectorizer.fit_transform(data)
# tfidf_vector
# print(count_vectorizer.vocabulary_)
# array=X.toarray()
# print(array)
# for x in array:
#     for i in x:
#         if i!=0:print(i)

X_train = count_vectorizer.fit_transform(data)
array=X_train.toarray()
print(len(array_train))

# print("Vocabulary size: {}".format(len(count_vectorizer.vocabulary_)))
# print("X_train:\n{}".format(repr(X_train)))
#
#
# feature_names = count_vectorizer.get_feature_names()
# print("Number of features: {}".format(len(feature_names)))


# for line in data_negative.splitlines():
#     print(line)
#     list=[]
#     list.append(line)
#     X=count_vectorizer.fit_transform(list)
#     np.array()
# word_negative=getWord(data_negative)

param_grid = {'C': [0.001, 0.01, 0.1, 1, 10]}
grid = GridSearchCV(LogisticRegression(), param_grid, cv=5)
grid.fit(tf_idf, array_train)

print("Best cross-validation score: {:.2f}".format(grid.best_score_))
print("Best parameters: ", grid.best_params_)
print("Best estimator: ", grid.best_estimator_)
lr = grid.best_estimator_
lr.fit(X_train, array_train)


pos = ["OK, so the musical pieces were poorly written and generally poorly sung (though Walken and Marner, particularly Walken, sounded pretty good). And so they shattered the fourth wall at the end by having the king and his nobles sing about the "'battle'" with the ogre, and praise the efforts of Puss in Boots when they by rights shouldn't have even known about it.<br /><br />Who cares? It's Christopher Freakin' Walken, doing a movie based on a fairy tale, and he sings and dances. His acting style fits the role very well as the devious, mischievous Puss who seems to get his master into deeper and deeper trouble but in fact has a plan he's thought about seven or eight moves in advance. And if you've ever seen Walken in any of his villainous roles, you *know* the ogre bit the dust HARD at the end when Walken got him into his trap.<br /><br />A fun film, and a must-see for anyone who enjoys the unique style of Christopher Walken."]
print("Pos prediction: {}". format(lr.predict(tfidf_vector.transform(pos))))
terms = tfidf_vector.get_feature_names()

# sum tfidf frequency of each term through documents
sums = X_train.sum(axis=0)

# connecting term to its sums frequency
data = []
for col, term in enumerate(terms):
    data.append( (term, sums[0,col] ))

ranking = pd.DataFrame(data, columns=['term','rank'])
print(ranking.sort_values('rank', ascending=True))
