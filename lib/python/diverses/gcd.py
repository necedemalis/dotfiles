def gcd(a,b):
    while a:
        a, b = b%a,a
    return b

print(gcd(15,10))

