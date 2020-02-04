from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
values=tokenizer.tokenize("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .")
for i in values:
    print(i)
