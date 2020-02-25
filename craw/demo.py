import os

path = '/home/phivantuan/Documents/craw/2549'

files = []
# r=root, d=directories, f = files
for r,f in os.walk(path):
    for file in f:
        if '.txt' in file:
            files.append(os.path.join(r, file))

for f in files:
    print(f)