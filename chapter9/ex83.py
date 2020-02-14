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
    for x in data:result += x.count(t+" "+c)+x.count(c+" "+t)
    return result

def calculate_f(t):
    result = 0
    for x in data:
        result+=x.count(t)
    return result

def calculate_N(t, c):
    result=0
    for x in data:
        result+=x.count(t)+x.count(c)
    return result
# print(calculate_f("Viet_Nam"))


# for name in list_country:
#     print(name+" : "+str(calculate_f(name)))
def matrix(t):
    for x in data:
        if t in x:
            array_c=x.partition(t)


    ft=calculate_f(t)

