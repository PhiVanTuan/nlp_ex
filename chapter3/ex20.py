import json
file= open("jawiki-country.json")
# str_json=file.read()
str=""
num=0
for f in file:
    if num==1:
        str=f
        break
    else:num+=1
print(str)
y=json.loads(str)
print(y["text"])
# print(str_json)
