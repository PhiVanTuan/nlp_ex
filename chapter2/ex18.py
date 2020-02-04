import operator
file=open("hightemp.txt")
col3=[]

for f in file:
    dic = {}
    dic["col1"]=f.split("\t")[0]
    dic["col2"]=f.split("\t")[1]
    dic["col3"]=f.split("\t")[2]
    dic["col4"]=f.split("\t")[3].replace("\n","")
    col3.append(dic)
# print(sorted(col3,key=lambda i: i["col3"],reverse=True))
col3.sort(key=lambda i: i["col3"],reverse=True)

print(col3)