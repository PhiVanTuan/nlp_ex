import pycountry

country = pycountry.countries
list_country = []
dict = {}
for x in country:
    name=x.name
    if ' ' in name:name = name.replace(' ', '_')
    list_country.append(name)

file = open("output2.txt")
text = ""
for line in file:
    for name in list_country:
        if name in line:
            array=line.partition(name)
            t1=" ".join(array[0].split()[-2:])
            t2=" ".join(array[2].split()[:2])
            if not t1 =="":t1+=" "
            if not t2 =="":name+=" "
            text+=t1+name+t2+"\n"
            print(t1+name+t2)
file.close()
file2=open("context.txt","w")
file2.write(text)
file2.close()
