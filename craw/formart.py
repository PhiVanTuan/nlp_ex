# import os
# import json
#
# path = '/home/phivantuan/Documents/craw2/'
#
# files = []
# # r=root, d=directories, f = files
# for r, d, f in os.walk(path):
#     for file in f:
#         if '.txt' in file:
#             files.append(os.path.join(r, file))
# oneStar = 0
# twoStar = 0
# threeStar = 0
# fourStar = 0
# fiveStar = 0
# label=""
# with open('review.txt','w') as review:
#         for f in files:
#             try:
#                 # print(f)
#                 data = json.loads(open(f).read())
#                 negative = data['1']
#                 negative.extend(data['2'])
#                 negative.extend(data['3'])
#                 neu = data['4']
#                 positive = data['5']
#                 oneStar += len(negative)
#                 fourStar += len(neu)
#                 fiveStar += len(positive)
#                 for one in negative:
#                     one=" ".join(one.splitlines())
#                     review.write(one +'\n')
#                     label+="-1\n"
#                 if (fourStar < 135000):
#                     for n in neu:
#                         n=" ".join(n.splitlines())
#                         review.write(n + '\n')
#                         label += "0\n"
#                 if fiveStar < 135000:
#                     for p in positive:
#                         p=" ".join(p.splitlines())
#                         review.write(p + '\n')
#                         label += "1\n"
#                 # print("oneStar :  " + str(oneStar) + "  twoStar :  " + str(twoStar) + "  threeStar :  " + str(
#                 #     threeStar) + "  fourStar :  " + str(fourStar) + "  fiveStar :  " + str(fiveStar))
#             except:
#                 print("error " + f)
#
# open('label.txt','w').write(label)
# print("FINAL :   oneStar :  " + str(oneStar) + "  fourStar :  " + str(fourStar) + "  fiveStar :  " + str(fiveStar))
