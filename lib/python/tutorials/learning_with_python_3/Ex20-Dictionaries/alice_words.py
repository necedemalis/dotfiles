

f = open ("/home/joecool/lib/python/tutorial/Ex20-Dictionaries/alice.txt")
text = f.read()
f.close()
print(f)
s = text.maketrans ("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\", "abcdefghijklmnopqrstuvwxyz                                          ")
cleaned_text = text.translate(s)

words = cleaned_text.split()



outfile = open ("/home/joecool/lib/python/tutorial/Ex20-Dictionaries/alice_words.txt", "w")
word_list = {}
for i in words:
        word_list[i] = word_list.get(i,0)+1
letter_list = list(word_list.items())
letter_list.sort()

#print ("Word\t","Count\n")
w = ""
for x in letter_list:
    if len(x[0]) >= 8:
        w = str(x[0]) + "\t" + str(x[1]) + "\n"
        outfile.write (w)
    else:
        w = str(x[0]) + "\t"+ "\t" + str(x[1]) + "\n"
        outfile.write (w)