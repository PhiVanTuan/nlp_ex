file=open("hightemp.txt")
lines = file.read().splitlines()
num_lines = sum(1 for line in file)
def n_line_end(n):
    for i in range(num_lines-n,num_lines,1):
        str=lines[i]
        print(str)
n_line_end(3)

