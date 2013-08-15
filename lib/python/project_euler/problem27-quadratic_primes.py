def isprime(number):
    '''Returns True if number is prime.'''
    prime = True
    for i in range (2, int(number**0.5)+1):
        if number%i == 0:
            prime = False
            break
    if prime:
        return True

def __main__():
    '''Find the product of the coefficients, a and b, for the quadratic expression [n² + an + b, where |a| < 1000 and |b| < 1000] that produces the maximum number of primes for consecutive values of n.'''
    longest_list = (0,0,0,)
    for a in range (-1000,1000):
        for b in range (-1000,1000):
            prime_list= []
            n = 0
            summe = n**2 + a*n + b
            if summe <= 0:
                continue
            while isprime(summe):
                prime_list.append(int(summe))
                n += 1
                summe = n**2 + a*n + b
                if summe <= 0:
                    break
                if len(prime_list) > longest_list[0]:
                    longest_list = (len(prime_list),a,b)

    sign = '+' if longest_list[1] >=0 else '-'
    sign2 = '+' if longest_list[2] >=0 else '-'
    print ("The quadratic formula n² {} {}n {} {} produces the maximum number of primes ({}). The product of a*b is {}.".format(sign,abs(longest_list[1]),sign2,abs(longest_list[2]),longest_list[0],(longest_list[1]*longest_list[2])))

import datetime
now = datetime.datetime.now()
if __name__ == __main__():
    __main__()
print(datetime.datetime.now() - now)
