import math
import datetime

def proper_divisors(max):
    '''Find proper divisors of numbers up to inclusive $max and build list with tuples (number, sum of divisors).'''
    divisor_list = {}

    for number in range(2,max+1):
        summe = 0
        div_list = {i for i in range(1,math.floor(math.sqrt(number))+1) if number%i==0}
        div_list2 = {number//i for i in div_list}
        div_list.update(div_list2)
        div_list.remove(number)
        summe = sum(div_list)
        #print (number,div_list)
        divisor_list[number] = summe
    return list(divisor_list.items())

def __main__(max):
    '''Evaluate sum of all amicable numbers under $max.'''
    summe2= 0
    summen_liste = proper_divisors(max)
    for i in summen_liste:
        (x,y) = i
        if (y,x) in summen_liste and y != x:
            print (x,':',y)
            summe2 += x
    print(summe2)

if __name__== '__main__':
    now = datetime.datetime.now()
    __main__(10000)
    print(datetime.datetime.now() - now)
