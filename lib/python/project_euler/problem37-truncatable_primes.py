'''
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''
import itertools

def isprime(number):
    '''Returns True if number is prime.'''
    prime = True
    if number == 1:
        return False
    for i in range (2, int(number**0.5)+1):
        if number%i == 0:
            prime = False
            break
    if prime:
        return True

def prime_generator():
    for number in itertools.count(10):
        prime = True
        for i in range(2,int(number**0.5)+1):
            if number%i == 0:
                prime = False
                break
        if prime:
            yield number

def truncate_lefttoright(number):
    '''Truncate prime from left to right recursively and check if new number is prime.'''
    next_number = number%10**(len(str(number))-1)
    if len(str(number))==1 and isprime(number):
        return True
    elif truncate_lefttoright(next_number) and isprime(number):
        return True

def truncate_righttoleft(number):
    '''Truncate prime from right to left recursively and check if new number is prime.'''
    next_number = number//10
    if len(str(number))==1 and isprime(number):
        return True
    elif truncate_righttoleft(next_number) and isprime(number):
        return True

def __main__():
    '''Find the sum of the only eleven primes that are both truncatable from left to right and right to left.'''
    summe = 0
    truncatable_primes = 0
    primes = prime_generator()
    while truncatable_primes < 11:
        for prime in primes:
            if truncate_lefttoright(prime) and truncate_righttoleft(prime):
                truncatable_primes += 1
                print(truncatable_primes,':',prime)
                summe += prime
            break
    print(''.join(['The sum of all 11 truncatable primes is ',str(summe),'.']))

if __name__ == '__main__':
    __main__()
