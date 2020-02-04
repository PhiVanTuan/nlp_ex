import re
from nltk.util import ngrams
s1="paraparaparadise"
s2="paragraph"

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

def union(lst1, lst2):
    final_list = list(set(lst1) | set(lst2))
    return final_list
print(union(ngram_character(s1,2),ngram_character(s2,2)))

def different(lst1,lst2):
    temp3 = [item for item in lst1 if item not in lst2]
    return  temp3
print(different(ngram_character(s1,2),ngram_character(s2,2)))

def intersection(lst1,lst2):
    temp3 = [item for item in lst1 if item in lst2]

    return  temp3
print(intersection(ngram_character(s1,2),ngram_character(s2,2)))