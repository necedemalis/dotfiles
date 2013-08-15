import itertools

def find_palindrome(summe):
    '''Find palindrome made from the list of products of two $max-digit numbers.'''
    while True:
        if summe[0] == summe[-1]:
            summe = summe[1:-1]
            if len(summe) <= 1:
                pali_list.append(x*y)
                break
        else:
            break

max = int(input('Largest palindrome product of how many digits?: '))

num_list = list(itertools.combinations(list(range(10**(max-1),10**max)),2))
pali_list = []

for x, y in num_list:
    summe = str(x*y)
    find_palindrome(summe)

pali_list.sort()
print ('The largest palindrome made from the product of two {}-digit numbers is {}.'.format(max,pali_list[-1]))
