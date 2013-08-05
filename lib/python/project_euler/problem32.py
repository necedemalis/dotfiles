def find_pandigital (multiplier,multiplicand):
    '''Find out if $multiplier*$multiplicand=summe == pandigital product from 1-9.'''
    for digit in str(multiplier):
        if digit not in str(multiplicand):
            summe = multiplier*multiplicand
            digits = {digit for i in (str(multiplier),str(multiplicand),str(summe)) for digit in i}
            if len(digits) == 9 and '0' not in digits:
                return summe

def __main__():
    '''Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.'''
    summen_set = set()
    for multiplier in range (2,99):
        min_range = 1000 if multiplier < 10 else 100
        for multiplicand in range(min_range,9999//multiplier):
            summe = find_pandigital(multiplier,multiplicand)
            if summe != None:
                print(multiplier,'*',multiplicand,'=',summe)
                summen_set.add(summe)
    print("\nErgebnis =",sum(summen_set))

if __name__ == '__main__':
    __main__()
