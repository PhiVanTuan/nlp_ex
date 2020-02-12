from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

import numpy as np
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
array=tf_idf.toarray()
array_train=[]
list=[]
for i in data_negative.splitlines():
    array_train.append(0)
for i in data_positive.splitlines():
    array_train.append(1)
print(list.append(array_train))
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


pos = ["I've seen this story before but my kids haven't. Boy with troubled past joins military, faces his past, falls in love and becomes a man. "
       "The mentor this time is played perfectly by Kevin Costner; An ordinary man with common everyday problems who lives an extraordinary "
       "conviction, to save lives. After losing his team he takes a teaching position training the next generation of heroes. The young troubled "
       "recruit is played by Kutcher. While his scenes with the local love interest are a tad stiff and don't generate enough heat to melt butter, "
       "he compliments Costner well. I never really understood Sela Ward as the neglected wife and felt she should of wanted Costner to quit out of "
       "concern for his safety as opposed to her selfish needs. But her presence on screen is a pleasure. The two unaccredited stars of this movie "
       "are the Coast Guard and the Sea. Both powerful forces which should not be taken for granted in real life or this movie. The movie has some "
       "slow spots and could have used the wasted 15 minutes to strengthen the character relationships. But it still works. The rescue scenes are "
       "intense and well filmed and edited to provide maximum impact. This movie earns the audience applause. And the applause of my two sons."]
print("Pos prediction: {}". format(lr.predict(tfidf_vector.transform(pos))))
