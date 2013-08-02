'''Find the sum of all numbers which are equal to the sum of the factorial of their digits.'''
from math import factorial

endsumme = 0
for x in range(3,2540161): #9!*7+1=highest possible number
    summe = 0
    for y in str(x):
        summe += factorial(int(y))
    if summe == x:
        endsumme += summe
print(endsumme)
