file = open("context.txt")
data=file.read().splitlines()
import pycountry

country = pycountry.countries
list_country = []
for x in country:
    name = x.name
    if ' ' in name: name = name.replace(' ', '_')
    list_country.append(name)


def calculate_f_t_c(t, c):
    result=0
    for x in data:
        if (t+" "+c) in x or (c+" "+t) in x:result+=1
    return result


def calculate_f(t):
    result = 0
    for x in data:
        result+=x.count(t)
    return result

def calculate_N(t, c):
    pass
# print(calculate_f("Viet_Nam"))

for name in list_country:
    print(name+" : "+str(calculate_f(name)))

