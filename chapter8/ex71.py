from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import nltk
stopWords = set(stopwords.words('english'))
data=open("sentiment.txt").read()
def checkStopword(str):
    if str in stopWords:return True
    else:return False
print(checkStopword("any"))
