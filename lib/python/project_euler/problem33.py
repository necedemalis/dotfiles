from functools import reduce

def canceller(numerator, denominator):
    '''Cancelling same number in numerator and denominator and yield quotient of new division.'''
    (num,denom) = ({numerator//10,numerator%10},{denominator//10,denominator%10})
    if num.isdisjoint(denom) == False: #müssen 1 gleiche Zahl haben
        if len(num.intersection(denom)) == 1: #nur 1 gleiche, nicht 2 gleiche (wie 34/43)
            quotient = list(num.difference(denom))[0]/list(denom.difference(num))[0]
            return quotient

def __main__():
    '''Yield denominator of lowest common terms of product of fractions, which are the same when cancelling same number in numerator and denominator (i.e 49/98 = 4/8, cancel 9).'''
    num_denom_list =[[],[]]
    for numerator in range (11,99):
        for denominator in range(numerator+1,100):
            if numerator%10 != 0 and denominator%10 != 0 and numerator%11 != 0 and denominator%11 != 0:
                if numerator/denominator == canceller(numerator,denominator):
                    print(numerator,'/',denominator)
                    num_denom_list[0].append(numerator)
                    num_denom_list[1].append(denominator)

    numerator = reduce(lambda x,y: x*y, num_denom_list[0]) #product of all numerators
    denominator = reduce(lambda x,y: x*y, num_denom_list[1]) #product of all denominators
    for i in range (numerator,1,-1): #Find lowest common terms
        if denominator%i == 0 and numerator%i == 0:
            print('-------')
            print('%02d' % (numerator//i),'/',denominator//i)
            break

if __name__ == '__main__':
    __main__()
