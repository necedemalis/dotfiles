import math
import itertools

def sum_all_divisors(number):
    '''Yield sum of all divisors of $number.'''
    l = [{i,number//i} for i in range(2,math.floor(math.sqrt(number))+1) if number%i == 0]
    return sum(itertools.chain.from_iterable(l))+1

def sum_combinations_of_numberlist(liste):
    '''Yield list of sums of all possible combinations of a two numbers in a $list.'''
    liste = list(itertools.combinations_with_replacement(liste,2))
    sum_set = {sum(i) for i in liste if sum(i) <= max}
    sum_list = list(sum_set)
    sum_list.sort()
    return(sum_list)

def find_missing_numbers(liste):
    '''Find missing integers starting from 1 in a $list up to $max.'''
    pos = 0
    missing_numbers_list = []
    for number in range(max+1):
        if number == liste[pos]:
            pos +=1
        else:
            missing_numbers_list.append(number)
    return missing_numbers_list

def __main__():
    '''Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.'''
    global max
    max = 28123 #all integers greater than 28123 can be written as sum of two abundant numbers
    abundant_numbers = [number for number in range(12,max+1) if sum_all_divisors(number) > number]
    sum_abundant_numbers_list = sum_combinations_of_numberlist(abundant_numbers)
    missing_numbers = find_missing_numbers(sum_abundant_numbers_list)
    endsumme = sum(missing_numbers)
    print(endsumme)

if __name__ == "__main__":
    __main__()
