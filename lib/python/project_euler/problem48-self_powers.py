'''Find the last ten digits of the series, 1¹ + 2² + 3³ + ... + 1000¹.'''

print(str(sum(i**i for i in range(1,1001)))[-10:])
