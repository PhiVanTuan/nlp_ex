from nltk.tokenize import sent_tokenize, word_tokenize
import warnings
from gensim.models import Word2Vec
from gensim.models import KeyedVectors
from gensim.test.utils import common_texts, get_tmpfile
warnings.filterwarnings(action='ignore')

word2vec = KeyedVectors.load_word2vec_format("/home/phivantuan/PycharmProjects/source-archive/word2vec/trunk/vectors.bin",binary=True)

def vec(s):
    return word2vec.wv[s]
def ex86():
    print(vec('United_States'))
def ex87():
    print(word2vec.similarity('United_States', 'U.S'))
# word2vec = Word2Vec(all_words, min_count=2)
# vocabulary = word2vec.wv.vocab
# print(vocabulary)
def ex88():
    sim_words = word2vec.wv.most_similar('England')
    print(sim_words)
def ex89():

    result2=word2vec.wv.most_similar(positive=['Spain', 'England','United_States'], negative=['London'],topn=50)
    print(result2)
# ex86()
sim_words = word2vec.wv.most_similar('cntt')
print(sim_words)