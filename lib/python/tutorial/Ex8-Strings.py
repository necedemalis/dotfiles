#prefixes="JKLMNOPQ"
#suffix="ack"
#for p in prefixes:
#    print (p+suffix)

friends = ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]
#print(friends[2:])


#word="Banana"
#if word < "Banana":
#    print("Your word, " + word + ", comes before banana.")
#elif word > "Banana":
#    print("Your word, " + word + ", comes after banana.")
#else:
#    print("Yes, we have no bananas!")


def remove_vowels (s):
    vowels="aeiouAEIOU"
    s_sans_vowels=""
    for x in s:
        if x not in vowels:
            s_sans_vowels +=x
    return s_sans_vowels

def find (strng, ch):
    ix=0
    while ix <len(strng):
        if strng[ix]==ch:
            return ix
        ix +=1
    return -1
    #print (find("Compscip", "p"))

def count_a(text):
    count=0
    for c in text:
            if c == "a":
                count +=1
    return(count)
#print(count_a("banana"))

def find2 (strng, ch, start):
    ix=start
    while ix < len(strng):
        if strng[ix]==ch:
            return ix
        ix +=1
    return -1
#print (find2("banana", "a", 2))




#Split-Function
ss = "Well I never did said Alice"
wds= ss.split()
#print(wds)


def remove_punctuation(s):
    import string
    s_without_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct
#print (remove_punctuation('"Well, I never did!", said Alice.'))

#layout=" {0:>4}{1:>6}{2:>6}{3:>8}{4:>13}{5:>24}"
#print(layout.format("i", "i**2", "i**3", "i**5", "i**10", "i**20"))
#for i in range (1,11):
#    print (layout.format(i, i**2,i**3,i**5,i**10,i**20))


#2
def duckling():
    prefixes = "JKLMNOPQ"
    suffix = "ack"
    for letter in prefixes:
        if letter =="O":
            print (letter + "u" + suffix)
        elif letter =="Q":
            print (letter + "u" + suffix)
        else:
            print(letter + suffix)




#3
def count_letters(n):
    count = 0
    for char in n:
        if char == "a":
            count += 1
    return count
#print (count_letters("banana"))


#5
def analyze_text(n,l):
    import string
    text_wo_p=""
    count=0
    ix=0
    count_e=0
    list_words =""
    list_nr=0
    #No punctuation
    for letter in n:
        if letter not in string.punctuation:
            text_wo_p += letter
    words_in_text=text_wo_p.split()
    #{0}
    for word in words_in_text:
        count +=1
        #{1}
        while ix < len(word):
            if word[ix]==l:
                count_e +=1
                list_words += (str(list_nr+1) +".)"+ word + "\n")
                list_nr +=1
                break
            ix +=1
        ix=0
    #{2}
    if count_e >0:
        perc=100/(count/count_e)
    else:
        perc=0
    #List of words
    split_list_words=list_words.split()
    print ("Your text contains {0} words, of which {1} ({2}%) contain an '{3}'.".format (count,count_e,perc,l))
    print ("These words are:\n",list_words)
text="""
Now rewrite the count_letters function so that instead 
of traversing the string, it repeatedly calls the find method, with the 
optional third parameter to locate new occurrences of the letter being 
counted.
"""
print (analyze_text (text,("c","o")))


#6
def mult_table (x,y):
    line =""
    head =""
    hline =""
#    strich=""
    for i in range (2,x+1):
        head= head + "{0:>6}".format(i)
#        for n in range (1,len(str(i))):
#            strich = strich + "-"
        hline= hline +"------"
    print ("{0:>10}".format(1) + head)
    print (" :--------"+ hline)
    for i in range (1,y+1):
        for j in range (1,x+1):
            line = line + "{0:>6}".format(i*j)
        print ("{0:<4}".format((str(i)+":"))+ line)
        line =""
#print (mult_table(8,1500))

#7
def reverse (n):
    l=len(n)-1
    rev=""
    while l !=0:
        rev= rev + n[l]
        l -= 1
    rev = rev +n[0]
    return rev
#print (reverse("aa"))
#8
def mirror (n):
    print (n+ reverse(n))
#print (mirror("happy"))

#9
def remove_letter (l,w):
    word_wo_l=""
    for i in (w):
        if i is not l:
            word_wo_l= word_wo_l + i
    return word_wo_l
#print (remove_letter("i", "Mississippi"))

#10
def is_palindrome (n):
    if n== reverse(n):
        print (True)
    else: print (False)
#print (is_palindrome("straw warts"))

#11
def count (ss,s):
    count =0
    ix=0
    ss_len=len(ss)
    while ix < (len(s)-ss_len+1):
        if s[ix:ix+ss_len]== ss:
            count +=1
        ix +=1
    return (count)
#print(count ("aaaa", "aaaaaaa"))
#12
def remove (ss,s):
    text=""
    count=0
    ix=0
    ss_len=len(ss)
    while ix < (len(s)-ss_len+1):
        if count ==0:
            if s[ix:ix+ss_len]!= ss:
                text= text + s[ix]
                ix +=1
            else: 
                ix += ss_len
                count=1
        elif count ==1:
                text= text + s[ix]
                ix +=1
    text =text + s[len(s)-ss_len+1:len(s)]
    print (text)
print (remove("ic", "bicycle"))
#13
def remove_all (ss,s):
    text=""
    count=0
    ix=0
    ss_len=len(ss)
    while ix < (len(s)-ss_len+1):
        if s[ix:ix+ss_len]!= ss:
            text= text + s[ix]
            ix +=1
        else: 
            ix += len(ss)
    text =text + s[len(s)-ss_len+1:len(s)]
    print (text)
#print (remove ("iss", "Mississippi"))
