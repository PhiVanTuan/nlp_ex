from nltk.tokenize import sent_tokenize, word_tokenize
import warnings
from gensim.models import Word2Vec

warnings.filterwarnings(action='ignore')
file=open("family.txt")
data=file.read().splitlines()
all_words=[word_tokenize(x) for x in data]
word2vec = Word2Vec(all_words, min_count=2)
def vec(s):
    return word2vec.wv[s]
for line in data:
    text=line.split()
    result=vec(text[1]) - vec(text[0]) + vec(text[2])
    result2=word2vec.wv.most_similar(positive=[text[1], text[2]], negative=[text[0]])
    print("Wordvector " + text[1] + " - " + text[0]+" + "+text[2])
    print(result)
    print(result2)


