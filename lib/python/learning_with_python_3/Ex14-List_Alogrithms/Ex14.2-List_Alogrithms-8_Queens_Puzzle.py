from unit_tester import test

#14.8
def share_diagonal(x0,y0,x1,y1):
    dy= abs(y1-y0)
    dx= abs(x1-x0)
    return dx == dy
test(not share_diagonal(5,2,2,0))
test(share_diagonal(5,2,3,0))
test(share_diagonal(5,2,4,3))
test(share_diagonal(5,2,4,1))

def col_clashes (bs,c):
    for i in range(c):
        if share_diagonal (i, bs[i],c, bs[c]):
            return True


    return False
test(not col_clashes([6,4,2,0,5], 4))
test(not col_clashes([6,4,2,0,5,7,1,3], 7))

def has_clashes(the_board):
    for col in range(1,len(the_board)):
        if col_clashes(the_board,col):
            return True
    return False
test(not has_clashes([6,4,2,0,5,7,1,3])) # Solution from above
test(has_clashes([4,6,2,0,5,7,1,3]))     # Swap rows of first two
test(has_clashes([0,1,2,3]))             # Try small 4x4 board
test(not has_clashes([2,0,3,1]))         # Solution to 4x4 case

#14.9
def main ():
    import random
    import time
    t0= time.clock()
    rng = random.Random()
    bd=list(range(8))
    num_found = 0
    tries = 0
    all_tries=0
    while num_found < 10:
        rng.shuffle(bd)
        tries +=1
        if not has_clashes(bd):
            print ("Found solution {0} in {1} tries.".format(bd,tries))
            all_tries += tries
            tries = 0
            num_found +=1
    t1=time.clock()
    average= all_tries//13
    print ("This operation took {0:.4f} seconds of your precious time. It took {1} average tries per solution.".format(t1-t0,average))
#main ()


#Exercises
#Ex3
def search_linear(xs, target):
    """ Find and return the index of target in sequence xs """
    for i in xs:
       if i == target:
           return True
    return False

def main2 ():
    import random
    import time
    t0= time.clock()
    rng = random.Random()
    found_solutions = [[8,9],[0,1]]
    bd=list(range(8))
    num_found = 0
    tries = 0
    all_tries=0
    test=0
    while num_found < 10:
        rng.shuffle(bd)
        tries +=1
        if not has_clashes(bd) and not search_linear(found_solutions,bd):
            found_solutions.append(bd)
            print ("Found solution {0} in {1} tries.".format(bd,tries))
            all_tries += tries
            tries = 0
            num_found +=1
            print (found_solutions)
        rng.shuffle(bd)
    t1=time.clock()
    average= all_tries//8
    print ("This operation took {0:.4f} seconds of your precious time. It took {1} average tries per solution.".format(t1-t0,average))
#main2 ()

#Ex5
my_tickets = [ [ 7, 17, 37, 19, 23, 43],
               [ 7,  2, 13, 41, 31, 43],
               [ 2,  5,  7, 11, 13, 17],
               [13, 17, 37, 19, 23, 43] ]
#5a
def lotto_draw ():
    import random
    rng = random.Random ()
    lotto = []
    for i in range (6):
        i = rng.randrange (1,50)
        lotto.append(i)
    return lotto
lotto_draw()

#5b
def lotto_match (t,d):
    r=0
    for i in t:
        if d.count(i) >= 1:
            r= r + d.count(i)
    return r
test(lotto_match([42,4,7,11,1,13], [2,5,7,11,13,17]) == 3)

#5c
def lotto_matches (d,t):
    r=[]
    for x in t:
       a = lotto_match (x,d)
       r.append(a)
    return r
test(lotto_matches([42,4,7,11,1,13], my_tickets) == [1,2,3,1])

#5e
def is_prime (n):
    if n == 1 or n == 0:
        return False
    for i in range (2,n):
        if n%i==0:
            return False
    return True
#5d
def primes_in (l):
    c=0
    for i in l:
        if is_prime (i):
            c += 1
    return c
test(primes_in([42, 4, 7, 11, 1, 13]) == 3)

#5e
def remove_adjacent_dups(xs):
    result = []
    most_recent_elem = None
    for e in xs:
        if e != most_recent_elem:
            result.append(e)
            most_recent_elem = e
    return result

def prime_misses (t):
    p =[] #liste an primzahlen
    l = [] #Gesamtliste Lottozahle
    mp = [] #Liste and fehlenden Primzahlen
    for x in (range(50)):
        if is_prime (x):
            p.append(x)

    for i in t:
        l.extend (i)
    l.sort ()
    l = remove_adjacent_dups(l)
    for i in p:
        if l.count(i) ==0:
            mp.append(i)
    return mp
test(prime_misses(my_tickets) == [3, 29, 47])
def good_luck ():
    picks = 5
    count = 0
    tries = 0
    t = my_tickets
    all_tries = 0
    while count < 20:
        d = lotto_draw ()
        tries += 1
        a = lotto_matches (d,t)
        if a.count (picks) >= 1:
            count = count + a.count(picks)
            print (d)
            print ("One ticket had {1} correct picks after {2} tries.".format (a,picks, tries))
            all_tries += tries
            tries=0
    average = all_tries//20
    print ("The computer scientist needed {0} average tries per ticket.".format(average))
good_luck()





