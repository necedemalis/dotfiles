sentence=''
with open ('02.txt') as a_file:
    for line in a_file:
        for letter in line:
            if ord(letter) >= 97 and ord(letter) <= 122:
                sentence += letter
print(sentence)
