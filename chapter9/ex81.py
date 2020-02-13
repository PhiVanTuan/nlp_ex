import pycountry
import re

country = pycountry.countries
list_country = []
dict = {}
for x in country:
    if ' ' in x.name:
        name = x.name.replace(' ', '_')
        dict[x.name] = name
print(dict)
file = open("ouput.txt")
text = ""
for line in file:
    for key, value in dict.items():
        if key in line:
            print(key)
            line=line.replace(key, value)
    text += line
    print(line)
    
file.close()
file2=open("output2.txt","w")
file2.write(text)
file2.close()
