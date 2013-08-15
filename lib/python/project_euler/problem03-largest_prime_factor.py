def prime_factors(max):
    nr = max
    highest = 0
    prim_list = []
    for num in range (2,max):
        prime = True
        for i in range(2,num):
            if num%i == 0:
                prime = False
        if prime:
            prim_list.append(num)
            for prime in prim_list:
                if max%prime == 0:
                    highest = prime
                    max = max/prime
        if max == 1:
            break

    print('The largest prime factor of {} is {}.'. format(nr,highest))

from datetime import datetime
startTime = datetime.now()
prime_factors(600851475143)
print(datetime.now()-startTime)
