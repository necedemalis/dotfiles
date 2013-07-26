def name_scores():
    name_list = []
    sum_list = []

    with open ('names.txt', encoding = 'utf-8') as a_file:
        a_text = a_file.read()
        cleaned_text = a_text.replace('"','')
        name_list = cleaned_text.split(',')
    name_list.sort()

    for name in name_list:
        summe = 0
        for letter in name:
            summe += ord(letter) - 64
        sum_list.append(summe * (name_list.index(name) + 1))

    print(sum(sum_list))

name_scores()
