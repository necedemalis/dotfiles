sentence=''
with open ('03.txt') as a_file:
    for line in a_file:
        for letter_number in range(len(line)-3):
            x= 0
            if ord(line[letter_number]) >= 97 and ord(line[letter_number]) <= 122:
                for i in range(1,4):
                    if ord(line[letter_number-i]) >= 65 and ord(line[letter_number-i]) <= 90:
                        if ord(line[letter_number+i]) >= 65 and ord(line[letter_number+i]) <= 90:
                            x += 1
                if x== 3:
                    if ord(line[letter_number-4]) >= 97 and ord(line[letter_number-4]) <= 122:
                        if ord(line[letter_number+4]) >= 97 and ord(line[letter_number+4]) <= 122:
                            sentence += line[letter_number]
print(sentence)
