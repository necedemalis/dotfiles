import time
from math import sqrt,floor

def triangular_number_div(max):
    '''Find value of the first triangle number (1+2+3+4...) to have over five hundred divisors.'''

    triangular_number=0; natural_number=1; divisors = 0

    while divisors <= max:
        triangular_number += natural_number
        div_list = set(i for i in range(1,floor(sqrt(triangular_number))+1) if triangular_number%i==0)
        higher_div_list = set(triangular_number//i for i in div_list)
        div_list.update(higher_div_list)
        divisors = len(div_list)
        natural_number += 1

    print(triangular_number)

now = time.time()
triangular_number_div(500)
print(time.time()-now)
