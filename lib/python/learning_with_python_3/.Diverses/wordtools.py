from unit_tester import test
def cleanword (s):
    pun = "!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"
    new_word=""
    for i in s:
        if i not in pun:
            new_word = new_word + i
    return new_word

test(cleanword("what?") == "what")
test(cleanword("'now!'") == "now")
test(cleanword("?+='w-o-r-d!,@$()'") ==  "word")

def has_dashdash(s):
    dash="--"
    if dash not in s:
        return False
    else:
        return True

test(has_dashdash("distance--but"))
test(not has_dashdash("several"))
test(has_dashdash("spoke--"))
test(has_dashdash("distance--but"))
test(not has_dashdash("-yo-yo-"))

def wordcount (a,l):
    count=0
    for i in l:
        if i == a:
            count+=1
    return count
test(wordcount("now", ["now","is","time","is","now","is","is"]) == 2)
test(wordcount("is", ["now","is","time","is","now","the","is"]) == 3)
test(wordcount("time", ["now","is","time","is","now","is","is"]) == 1)
test(wordcount("frog", ["now","is","time","is","now","is","is"]) == 0)

def wordset (l):
    new_list=[]
    for i in l:
        if i not in new_list:
            new_list.append(i)
    new_list.sort()
    return new_list

test(wordset(["now", "is", "time", "is", "now", "is", "is"]) ==
      ["is", "now", "time"])
test(wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) ==
      ["I", "a", "am", "is"])
test(wordset(["or", "a", "am", "is", "are", "be", "but", "am"]) ==
      ["a", "am", "are", "be", "but", "is", "or"])

def longestword (w):
    x= 0
    for i in w:
        if x < len (i):
            x=len(i)
    return x

test(longestword(["a", "apple", "pear", "grape"]) == 5)
test(longestword(["a", "am", "I", "be"]) == 2)
test(longestword(["this","supercalifragilisticexpialidocious"]) == 34)
test(longestword([ ]) == 0)
