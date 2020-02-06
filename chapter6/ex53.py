import stanfordnlp
import pandas as pd
from pycorenlp import StanfordCoreNLP
#extract lemma
def extract_lemma(doc):
    parsed_text = {'word':[], 'lemma':[],'pos':[]}
    for sent in doc.sentences:
        for wrd in sent.words:
            #extract text and lemma
            parsed_text['word'].append(wrd.text)
            parsed_text['lemma'].append(wrd.lemma)
            parsed_text['pos'].append(wrd.pos)
    #return a dataframe
    return pd.DataFrame(parsed_text)

#call the function on doc

nlp = stanfordnlp.Pipeline(processors = "tokenize,mwt,lemma,pos")
str=open("nlp.txt").read()
docs=nlp(str)
print(extract_lemma(docs))
# for doc in docs.sentences:
#     token_string=doc.tokens_string()
#     print(token_string)

