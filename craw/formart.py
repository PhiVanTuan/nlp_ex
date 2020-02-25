import os
import json
path = '/home/phivantuan/Documents/craw3/'

files = []
# r=root, d=directories, f = files
for r,d,f in os.walk(path):
    for file in f:
        if '.txt' in file:
            files.append(os.path.join(r, file))
oneStar=0
twoStar=0
threeStar=0
fourStar=0
fiveStar=0
for f in files:
    try:
        data=json.loads(open(f).read())
        oneStar+=len(data['1'])
        twoStar+=len(data['2'])
        threeStar+=len(data['3'])
        fourStar+=len(data['4'])
        fiveStar+=len(data['5'])
    except:
        print(f)

print("oneStar :  "+str(oneStar)+ "  twoStar :  "+str(twoStar)+"  threeStar :  "+str(threeStar)+"  fourStar :  "+str(fourStar)+"  fiveStar :  "+str(fiveStar))