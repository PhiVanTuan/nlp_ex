file=open("hightemp.txt")
file1 = open("col1.txt", "w")
file2 = open("col2.txt", "w")
col1=""
col2=""
for f in file:
    col1+=(f.split("\t")[0])+"\n"
    col2+=(f.split("\t")[1])+"\n"
    print(f.split("\t"))
file1.write(col1)
file2.write(col2)
file1.close()
file2.close()