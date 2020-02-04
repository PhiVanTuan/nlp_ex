from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
values=tokenizer.tokenize("Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.")
data = {}
for i in range(len(values)):
    if i==1 or i==5 or i== 6 or i==7 or i== 8 or i== 9 or i== 15 or i== 16 or i== 19:
        data[i]=values[i][0]
    else : data[i]=values[i][:2]
print(data)
