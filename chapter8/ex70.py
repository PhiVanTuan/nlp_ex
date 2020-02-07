
# with codecs.open('rt-polarity.pos', encoding='latin-1') as f:
#     for line in f:
#         print(repr(line))
pos=open("rt-polarity.pos",encoding='latin-1')
neg=open("rt-polarity.neg",encoding='latin-1')
str_pos=""
str_neg=""
sentiment=open("sentiment.txt","w")
for p in pos:
    str_pos+="1 "+p
for n in neg:
    str_neg+="-1 "+n
sentiment.write(str_pos+str_neg)
