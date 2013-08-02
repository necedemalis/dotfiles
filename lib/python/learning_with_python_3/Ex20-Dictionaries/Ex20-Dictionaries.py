from unit_tester import test


eng2sp = {}
eng2sp["one"] = "uno"
eng2sp["two"] = "dos"

#20.2
for k in eng2sp.keys():
    print ("Got key" , k ,"which maps to value", eng2sp[k])

print(list(eng2sp.keys()))
print(list(eng2sp.values()))
print(list(eng2sp.items()))


#20.5
alreadyknown = {0: 0, 1: 1}

def fib (n):
    if n not in alreadyknown:
        new_value = fib(n-1) + fib(n-2)
        alreadyknown[n] = new_value
        print (alreadyknown)
    return alreadyknown[n]
#print(fib (8))


#20.6
letter_counts = {}
for letter in "Mississippi":
    letter_counts[letter] = letter_counts.get(letter,0)+1
letter_items = list(letter_counts.items())
letter_items.sort()
#print (letter_items)


#Exercises
#1
def letter_table (n):
    letters = {}
    s = n.maketrans ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz")
    cleaned_text = n.translate(s)
    st = cleaned_text.split()
    for l in st:
        for x in l:
            letters[x] = letters.get(x,0)+1
    letter_list = list(letters.items())
    letter_list.sort()
    for (x,y) in letter_list:
        print (x,y)
letter_table("ThiS is String with Upper and lower case Letters")

#2
def add_fruit(inventory, fruit, quantity=0):
    inventory[fruit] = inventory.get(fruit,0) + quantity
    return

new_inventory = {}
add_fruit(new_inventory, "strawberries", 10)
test("strawberries" in new_inventory)
test(new_inventory["strawberries"] == 10)
add_fruit(new_inventory, "strawberries", 25)
test(new_inventory["strawberries"] == 35)

#3

