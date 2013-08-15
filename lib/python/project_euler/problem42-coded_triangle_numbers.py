'''
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.
Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
'''

from math import sqrt

def main():
    total = 0
    number_list = []
    with open ('problem42.txt') as a_file:
        a_text = a_file.read()
    cleaned_text = a_text.replace('"','')
    word_list = cleaned_text.split(',')
    for word in word_list:
        summe = 0
        for letter in word:
            summe += ord(letter)-64
        number_list.append(summe)

    for number in number_list:
        triangle = (sqrt(8*number+1)-1)/2
        if triangle/int(triangle) == 1.0: # Check if triangle
            total += 1

    print(total)

if __name__ == '__main__':
    main()
