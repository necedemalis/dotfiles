def findmultiples(n):
    sum = 0
    n_list = list(range(1,n))

    for i in n_list:
            if i%3 == 0 or i%5 == 0:
                sum += i

    return sum

print(findmultiples(1000))
