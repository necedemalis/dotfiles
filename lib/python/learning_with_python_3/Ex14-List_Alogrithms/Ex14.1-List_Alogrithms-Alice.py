from unit_tester import test

#14.2
def search_linear(xs, target):
    """ Find and return the index of target in sequence xs """
    for (i, v) in enumerate(xs):
       if v == target:
           return i
    return -1

friends = ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]
test(search_linear(friends, "Zoe") == 1)
test(search_linear(friends, "Joe") == 0)
test(search_linear(friends, "Paris") == 6)
test(search_linear(friends, "Bill") == -1)

#14.3
def find_unknown_words(vocab, wds):
    """ Return a list of words in wds that do not occur in vocab """
    result = []
    for w in wds:
        if (search_linear(vocab, w) < 0):
            result.append(w)
    return result
vocab = ["apple", "boy", "dog", "down",
                          "fell", "girl", "grass", "the", "tree"]
book_words = "the apple fell from the tree to the grass".split()
test(find_unknown_words(vocab, book_words) == ["from", "to"])
test(find_unknown_words([], book_words) == book_words)
test(find_unknown_words(vocab, ["the", "boy", "fell"]) == [])

def text_to_words(the_text):
    my_substitutions = the_text.maketrans(
      # If you find any of these
      "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
      # Replace them by these
      "abcdefghijklmnopqrstuvwxyz                                          ")

    cleaned_text = the_text.translate(my_substitutions)
    wds = cleaned_text.split()
    return wds
test(text_to_words("My name is Earl!") == ["my", "name", "is", "earl"])
test(text_to_words('"Well, I never!", said Alice.') ==
                             ["well", "i", "never", "said", "alice"])

def load_words_from_file(filename):
    f = open(filename,"r")
    file_content = f.read()
    f.close()
    wds = text_to_words(file_content)
    return wds
bigger_vocab= load_words_from_file("vocab.txt")
print ("There are {0} words in the vocab, starting with\n{1} ".format
       (len(bigger_vocab),bigger_vocab[:6]))

book_words = load_words_from_file("alice_in_wonderland.txt")
print("There are {0} words in the book, in the first 10 are\n{1}".format (len(book_words),
                                                                           book_words[:10]))

import time
t0 =time.clock()
#missing_words = find_unknown_words(bigger_vocab,book_words)
t1=time.clock()
#print("There are {0} unknown words.".format(len(missing_words)))
print("That took {0:4f} seconds.".format(t1-t0))

#14.4
def search_binary (xs,target):
    lb=0
    ub=len(xs)
    while True:
        if lb == ub:
            return -1

        mid_index = (lb + ub) // 2
        
        item_at_mid = xs[mid_index]

        print ("ROI[{0}:{1}](size={2}),probed='{3}', tartget='{2}'".format(lb, ub, ub-lb,
                                                                           item_at_mid,
                                                                           target))
        if item_at_mid == target:
            return mid_index
        if item_at_mid < target:
            lb = mid_index + 1
        else:
            ub = mid_index
xs = [2,3,5,7,11,13,17,23,29,31,37,43,47,53]
test(search_binary(xs, 20) == -1)
test(search_binary(xs, 99) == -1)
test(search_binary(xs, 1) == -1)
#for (i, v) in enumerate(xs):
#    test(search_binary(xs, v) == i)

def find_unknown_words2(vocab, wds):
    """ Return a list of words in wds that do not occur in vocab """
    result = []
    for w in wds:
        if (search_binary(vocab, w) < 0):
            result.append(w)
    return result
t0 =time.clock()
#missing_words = find_unknown_words2(bigger_vocab,book_words)
t1=time.clock()
#print("There are {0} unknown words.".format(len(missing_words)))
print("That took {0:4f} seconds.".format(t1-t0))
#search_binary(bigger_vocab, "magic")

#14.5
def remove_adjacent_dups(xs):
    result = []
    most_recent_elem = None
    for e in xs:
        if e != most_recent_elem:
            result.append(e)
            most_recent_elem = e
    return result
test(remove_adjacent_dups([1,2,3,3,3,3,5,6,9,9]) == [1,2,3,5,6,9])
test(remove_adjacent_dups([]) == [])
test(remove_adjacent_dups(["a", "big", "big", "bite", "dog"]) ==
                                   ["a", "big", "bite", "dog"])
all_words = load_words_from_file("alice_in_wonderland.txt")
all_words.sort()
book_words = remove_adjacent_dups(all_words)
print("There are {0} words in the book. Only {1} are unique.".format
      (len(all_words),len(book_words)))
print ("The first 10 words are\n{0}".format(book_words[:10]))

#14.6
def merge (xs,ys):
    result=[]
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):
            result.extend(ys[yi:])
            return result

        if yi >=len(ys):
            result.extend(xs[xi:])
            return result

        if xs[xi] <= ys[yi]:
            result.append(xs[xi])
            xi += 1

        else:
            result.append(ys[yi])
            yi += 1
xs = [1,3,5,7,9,11,13,15,17,19]
ys = [4,8,12,16,20,24]
zs = xs+ys
zs.sort()
test(merge(xs, []) == xs)
test(merge([], ys) == ys)
test(merge([], []) == [])
test(merge(xs, ys) == zs)
test(merge([1,2,3], [3,4,5]) == [1,2,3,3,4,5])
test(merge(["a", "big", "cat"], ["big", "bite", "dog"]) ==
               ["a", "big", "big", "bite", "cat", "dog"])

#14.7
def find_unknowns_merge_pattern(vocab,wds):
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(vocab):
            result.extend(wds[yi:])
            return result
        if yi >= len(wds):
            return result

        if vocab[xi] == wds[yi]:
            yi +=1
        elif vocab[xi] < wds[yi]:
            xi += 1
        else:
            result.append(wds[yi])
            yi +=1

all_words = load_words_from_file("alice_in_wonderland.txt")
t0= time.clock()
all_words.sort()
book_words = remove_adjacent_dups (all_words)
missing_words = find_unknowns_merge_pattern (bigger_vocab, book_words)
t1= time.clock()
print ("There are {0} unkown words.".format (len(missing_words)))
print ("That took {0:.4f} seconds.".format (t0-t1))
g = open ("unknown_words.txt", "w")
for v in missing_words:
    g.write(v)
    g.write("\n")


#14.11 - Exercises
#1.a
def find_words_in_both_lists(vocab,wds):
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(vocab):
            #result.extend(wds[yi:])
            return result
        if yi >= len(wds):
            return result

        if vocab[xi] == wds[yi]:
            result.append(vocab[xi])
            yi +=1
        elif vocab[xi] < wds[yi]:
            xi += 1
        else:
            yi +=1
all_words = load_words_from_file("test1.txt")
all_words.sort()
book_words = remove_adjacent_dups (all_words)
voca = load_words_from_file("test2.txt")
missing_words = find_words_in_both_lists (voca, book_words)
print ("There are {0} words in both lists.".format (len(missing_words)))
print (missing_words)

#1.b
def find_words_in_first_list(vocab,wds):
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(vocab):
            
            return result
        if yi >= len(wds):
            result.extend(vocab[xi:])
            return result

        if vocab[xi] == wds[yi]:
            xi +=1
        elif vocab[xi] < wds[yi]:
            result.append(vocab[xi])
            xi += 1
        else:
            yi +=1
all_words = load_words_from_file("test1.txt")
all_words.sort()
book_words = remove_adjacent_dups (all_words)
voca = load_words_from_file("test2.txt")
missing_words = find_words_in_first_list (voca, book_words)
print ("There are {0} unique words in the first list.".format (len(missing_words)))
print (missing_words)

#1.bagdiff
def bagdiff(vocab,wds):
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(vocab):
            
            return result
        if yi >= len(wds):
            result.extend(vocab[xi:])
            return result

        if vocab[xi] == wds[yi]:
            yi +=1
            xi +=1
        elif vocab[xi] < wds[yi]:
            result.append(vocab[xi])
            xi += 1
        else:
            yi +=1
all_words = load_words_from_file("test1.txt")
all_words.sort()
book_words = remove_adjacent_dups (all_words)
voca = load_words_from_file("test2.txt")
missing_words = bagdiff(voca, book_words)
print ("There are {0} words left after some serious bagdiffing.".format (len(missing_words)))
print (missing_words)
