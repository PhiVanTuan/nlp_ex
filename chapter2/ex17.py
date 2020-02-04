file=open("col1.txt")
result=[]
for f in file:
    result.append(f.replace("\n",""))
print(result)
print(set(result))