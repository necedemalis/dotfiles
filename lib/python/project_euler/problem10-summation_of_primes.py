import math

def sum_of_primes_below(max):
    '''Find the sum of all the primes below two million'''

    numbers_list = list(range(2,max))
    sum=0
    for num in numbers_list:
        prime = True
        for i in range(2,math.floor(num**0.5)+1): #if we cannot find a number f less than or equal n that divides n then n is prime
            if num%i==0:
                prime = False
                break
        if prime:
            sum += num

    print(sum)

from datetime import datetime
now = datetime.now()
sum_of_primes_below(2000000)
print(datetime.now()-now)
