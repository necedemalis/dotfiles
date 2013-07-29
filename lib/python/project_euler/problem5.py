def smallest_multiple(max):
    '''Find the smallest positive number that is evenly divisible by all of the numbers from 1 to 20.'''

    divisor = max
    dividend = 1
    while True:
        if divisor == 3:
            break
        if dividend%divisor == 0:
            divisor -= 1
        else:
            dividend += 1
            divisor = max
    return dividend

from datetime import datetime
start_time = datetime.now()
print(smallest_multiple(20))
print(datetime.now() - start_time)
