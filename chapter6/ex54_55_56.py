from stanfordnlp.server import CoreNLPClient
import os
os.environ["CORENLP_HOME"] = r'\stanford-corenlp-full-2018-10-05'
print('---')
print('input text')
print('')
text = open("nlp.txt").read()
print(text)
# set up the client
print('---')
print('starting up Java Stanford CoreNLP Server...')
# set up the client
with CoreNLPClient(annotators=['tokenize','ssplit','pos','lemma','ner','depparse','coref'], timeout=3000000, memory='16G') as client:
    # submit the request to the server
    ann = client.annotate(text)
    # get the first sentence
    sentence = ann.sentence[0]
    print(sentence)