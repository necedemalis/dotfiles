def main ():
    '''Find largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1.'''
    highest = 0
    for number in range (1,9999):
        concatenated_product = ""
        for multiplier in range(1,100):
            product = number*multiplier
            concatenated_product += str(product)
            if len(concatenated_product) >= 9:
                break
        digits = {i for i in concatenated_product if len(concatenated_product) == 9}
        if len(digits) == 9 and '0' not in digits and int(concatenated_product) > highest:
            highest = int(concatenated_product)

    print (highest)

if __name__ == '__main__':
    main()
