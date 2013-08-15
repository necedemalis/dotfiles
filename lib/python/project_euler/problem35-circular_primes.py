def isprime(number):
    '''Returns True if number is prime.'''
    prime = True
    for i in range (2, int(number**0.5)+1):
        if number%i == 0:
            prime = False
            break
    if prime:
        return True

def prime_generator(max):
    for number in range(2,max):
        prime = True
        for i in range(2,int(number**0.5)+1):
            if number%i == 0:
                prime = False
                break
        if prime:
            yield number

from datetime import datetime
now = datetime.now()
prime_gen = prime_generator(1000000)
summe = 0
for prime in prime_gen:
    digits = [i for i in str(prime)]
    circular = True
    for i in range(1,len(digits)):
        x = digits [i:]
        y = digits [:i]
        if isprime(int(''.join(x+y))):
            pass
        else:
            circular = False
            break
    if circular:
        summe += 1

print(summe)
print(datetime.now() - now)
