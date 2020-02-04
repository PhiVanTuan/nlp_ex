file=open("hightemp.txt")
def n_line(n):
    for i in range(n):
        print(file.readline())
n_line(5)