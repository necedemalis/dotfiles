'''Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.'''
from decimal import Decimal, getcontext
getcontext().prec = 5000

def repeater(number):
    '''Yields lenght of a recurring cycle for a given string.'''
    recurring_cycles={0:number[0]}
    if len(number) > 1:
        for i in range(1, len(number)):
            for key in recurring_cycles:
                if recurring_cycles[key] != number[i:i+len(recurring_cycles[key])]:
                    recurring_cycles[key] += number[i]
                else: #Recurring?
                    times_recurring = 0
                    for n in range(4):
                        if recurring_cycles[key] == number[i+(len(recurring_cycles[key])*n):i+(len(recurring_cycles[key])*(n+1))]:
                            times_recurring += 1
                    if times_recurring == 4:
                        return len(recurring_cycles[key])
            recurring_cycles[i] = number[i]
    else:
        return 0

highest = (0,0)
for number in range (2,1000):
    fractions = str(Decimal(1)/Decimal(number))[2:]
    length_cycle = repeater(fractions)
    if length_cycle == None:
        length_cycle = 0
    if length_cycle > highest[1]:
        highest = (number,length_cycle)
print('d =',highest[0],'\nLength of recurring cycle:',highest[1])
