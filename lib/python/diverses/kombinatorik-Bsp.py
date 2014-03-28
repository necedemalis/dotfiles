import itertools
count = 0
x = itertools.permutations("ADCHIU", 6)

for i in x:
    a = "".join(i)
    if "ICH" not in a and "DU" not in a:
        count += 1
print(count)


zahlen=[0,1,2,3,4,5,6,7,8,9]
c=0
for i in range(0,100000):
    n=(list(str(i)))
    for z in zahlen:
        if n.count(str(z)) >= 2:
            c += 1
            break
print(c)





y = itertools.product("0123456789",repeat=5)

zahlen=[0,1,2,3,4,5,6,7,8,9]
liste=[]
count2=0

for i in y:
    if list(i)[0] is not "0":
        liste.append(list(i))

print(len(liste))

for i in liste:
        for z in zahlen:
            if list(i).count(str(z)) >= 2:
                count2 += 1
                break

print(count2)


from math import factorial as f
x= ((f(9)/f(8))*(f(10)/f(7)))+((f(9)/f(8))*(f(10)/f(8)))+(f(9)/f(8)*(f(10)/f(9)))+(f(9)/f(8))+1
