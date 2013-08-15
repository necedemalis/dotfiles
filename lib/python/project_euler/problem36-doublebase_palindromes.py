#The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
#Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#(Please note that the palindromic number, in either base, may not include leading zeros.)

def is_palindrome(summe):
    '''Return True if string of number is palindrome.'''
    while True:
        if summe[0] == summe[-1]:
            summe = summe[1:-1]
            if len(summe) <= 1:
                return True
        else:
            break

def __main__():
    '''Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.'''
    summe = 0
    for number in range(1,1000000):
        if is_palindrome(str(number)):
            if is_palindrome(str(bin(number))[2:]):
                print(number,bin(number))
                summe += number
    print("The sum of all double-base palindromes under one million:",summe)

if __name__ == '__main__':
    __main__()
