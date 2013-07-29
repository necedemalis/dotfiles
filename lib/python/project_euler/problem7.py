from itertools import count
import math

def prime_gen(position):
    '''Find $position prime number.'''
    numbers = count(2)
    z=0
    for num in numbers:
        prime = True
        for i in range(2,math.floor(num**0.5)+1): #if we cannot find a number f less than or equal n that divides n then n is prime
            if num%i==0:
                prime = False
                break
        if prime:
            z += 1
        if z == position:
            print(z,num)
            break

prime_gen(10001)
