import re
import nltk
nltk.download('punkt')
from nltk.stem.porter import *

porterStemmer = PorterStemmer()

# sentence = "Provision Maximum multiply owed caring on go gone going was this"
# wordList = nltk.word_tokenize(sentence)
#
# stemWords = [porterStemmer.stem(word) for word in wordList]
#
# print(' '.join(stemWords))
str=open("nlp.txt").read()
x=re.split('[\\.][\\s^[A-Z]',str)
for y in x:
    z=re.split("\\s",y)
    stemWords = [porterStemmer.stem(word) for word in z]

    print(' '.join(stemWords))

    # for i in z:
    #     print(i)
