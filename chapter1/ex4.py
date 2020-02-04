from nltk.tokenize import word_tokenize

example="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
tokenized_sents = word_tokenize(example)
for str in tokenized_sents:
    print(str)
    print(len(str))
