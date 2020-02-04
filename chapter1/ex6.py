import re
from nltk.util import ngrams
s="paraparaparadise"

def ngram_word(s):
    s = s.lower()
    s = re.sub(r'[^a-zA-Z0-9\s]', ' ', s)
    tokens = [token for token in s.split(" ") if token != ""]
    output = list(ngrams(tokens, 2))
    print(output)
def ngram_character(s,ngram):
    output=[]
    for i in range(len(s)-ngram+1):
        output.append(s[i:i+ngram])
    return output
print(ngram_character(s,2))