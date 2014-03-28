count = 5
nummern =[]
for i in range(10000, 100000):
    if "1" not in str(i):
        nummern.append(i)
for n in nummern:
    if "2" not in str(n):
        count +=1
#print(count)

count2 = 0
for i in range(1000000, 10000000):
    if "0" in str(i):
        c=0
        for x in str(i):
            if x == "0":
                c += 1
        if c == 2:
            count2 +=1
print(count2)
