import re
file=open("questions-words.txt").read()
x=file.split(":")
result=""
for line in x:
    if "family" in line:
        result="\n".join(line.splitlines()[1:])
file2=open("family.txt","w")
file2.write(result)
file2.close()