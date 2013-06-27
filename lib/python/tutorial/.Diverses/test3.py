import math


def factorial (n):
    sum=n
    if n ==0:
        return 1
    else:
        while n !=1:
            sum=sum*(n-1)
            n -=1
    return sum



def estimate_pi():
    total = 0
    k = 0
    factor = 2 * math.sqrt(2) / 9801
    while True:
        num = factorial(4*k) * (1103 + 26390*k)
        den = factorial(k)**4 * 396**(4*k)
        term = factor * num / den
        total += term
        
        if abs(term) < 1e-15: break
        k += 1

    return 1 / total

print estimate_pi()
