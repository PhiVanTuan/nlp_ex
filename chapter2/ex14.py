file=open("hightemp.txt")
print(file.readline())
def n_line(n):
    for i in range(n):
        print(file.readline())
n_line(5)