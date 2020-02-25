import os
import json
import string
import re

path_baomoi = '/home/phivantuan/Documents/baomoi/cleaned/'
path_data_vn = '/home/phivantuan/Documents/data_vnexpress.txt'
path = '/home/phivantuan/PycharmProjects/source-archive/word2vec/trunk/'
path_vnexpresss = '/home/phivantuan/PycharmProjects/source-archive/word2vec/trunk/vnexpress.txt'
s = "tuan 1234.567"


def convert_baomoi():
    files = []
    for r, d, f in os.walk(path_baomoi):
        for file in f:
            if '.txt' in file:
                files.append(os.path.join(r, file))

    with open(path + "merge.txt", 'w') as outfile:
        for fname in files:
            try:
                with open(fname, errors="ignore") as infile:
                    for line in infile:
                        line = line.replace("_", " ")
                        line += " <punct> "
                        s = re.sub('\s+', ' ', line)
                        outfile.write(s)

            except:
                print(fname)
        with open(path_data_vn) as vn_file:
            for line in vn_file:
                s = line.lower()
                s = re.sub(r'[^\w\s]', ' <punct> ', s)
                s = re.sub(r'\n', ' <punct> ', s)
                s = re.sub(r'\d+', ' <number> ', s)
                s = re.sub('\s+', ' ', s)
                outfile.write(s)


def convert_vnexpress():
    with open(path + "vnexpress.txt", 'w') as outfile:
        with open(path_data_vn) as infile:
            for line in infile:
                s = line.lower()
                s = re.sub(r'[^\w\s\n]', ' <punct> ', s)
                s = re.sub(r'\d+', ' <number> ', s)
                s = re.sub('\s+', ' ', s)
                outfile.write(s)


convert_baomoi()

# def merge():
#     with open(path + "merge.txt", "w") as outfile:
#
#         with open(path + "output.txt") as baomoi:
#             for i in baomoi:
#                 outfile.write(i)
#             outfile.write(" ")
#         with open(path_vnexpresss) as infile:
#             for line in infile:
#                 outfile.write(line)
# convert_baomoi()
# s = re.sub(r'[^\w\s]', ' <punct> ', s)
# s=re.sub(r'\d+',' <number> ',s)
# s=re.sub('\s+',' ',s)

# print(s)
