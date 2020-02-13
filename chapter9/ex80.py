import string
import pycountry

def remove_punctuation(data):
    translator = str.maketrans('', '', string.punctuation)
    tokens = [w.translate(translator) for w in data]
    return tokens
file = open("enwiki-20150112-400-r10-105752.txt")
text = ""
for f in file:
    data=f.split()
    data=remove_punctuation(data)
    txt=" ".join(data)
    print(txt)
    text+=txt+"\n"
file=open("ouput.txt","w")
file.write(text)
file.close()
# print(text)


