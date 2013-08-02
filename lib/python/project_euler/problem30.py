def __main__():
    '''Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.'''

    endsumme = 0
    for number in range(2,1000000):
        summe = 0
        number = str(number)
        for digit in number:
            summe += int(digit)**5
        if summe == int(number):
            endsumme += summe
            print('\t',summe)

    print('\t','------')
    print('Summe = ',endsumme)

if __name__=="__main__":
    __main__()
