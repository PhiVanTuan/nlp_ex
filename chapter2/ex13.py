
file1=open("col1.txt")
file2=open("col2.txt")
result1=[]
result2=[]
n=0
value=""
for f in file1:
    result1.append(f)

for f in file2:
    value+=result1[n].replace("\n","")+"\t"+f
    n+=1
file3=open("col3.txt","w")
file3.write(value)
file3.close()