'''Work out the first ten digits of the sum of the 50-digit numbers in "problem13_numbers.txt".'''

summe=0
with open ('problem13_numbers.txt',encoding='utf-8') as a_file:
    for line in a_file:
        summe += int(line.rstrip())
print(str(summe)[:10])
