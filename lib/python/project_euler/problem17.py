numbers = {'unit_position': ['dummy','one','two','three','four','five','six','seven','eight','nine'],
           'ten-twenty': ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen'],
           'decimal_position': ['dummy','ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']}

def number_letters_count(max):
    '''Numbers from 1 to $max inclusive written out in words and number of letters summed up'''
    sum = 0
    for number in range(1,max+1):
        number_string = ''
        hundred_mark=False
        if number//1000 >0:
            number_string = number_string + numbers['unit_position'][number//1000] + 'thousand'
            number = number%1000
        if number//100 >0:
            number_string = number_string + numbers['unit_position'][number//100] + 'hundred'
            hundred_mark=True
            number = number%100
        if number//10 >0:
            if hundred_mark:
                number_string += 'and'
                hundred_mark=False
            if number >= 20:
                number_string += numbers['decimal_position'][number//10]
                number = number%10
            else:
                number_string += numbers['ten-twenty'][number%10]
                number = 0
        if number >0:
            if hundred_mark:
                number_string += 'and'
            number_string += numbers['unit_position'][number]

        sum += len(number_string)

    print(sum)

number_letters_count(1000)
