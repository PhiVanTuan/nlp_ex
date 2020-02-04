file=open("hightemp.txt")
lines = file.read().splitlines()
name="line"
i=1
for line in lines:
    nameFile=name+str(i)+".txt"
    open(nameFile,"w").write(line)
    i+=1