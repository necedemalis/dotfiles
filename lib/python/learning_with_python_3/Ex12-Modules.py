import random
cards= list(range(52))
print (cards)
rng =random.Random()
rng.shuffle(cards)
print (cards)

def make_random_ints(num, lower_bound,upper_bound):
	rg=random.Random()
	result=[]
	for i in range(num):
		result.append(rg.randrange(lower_bound,upper_bound))
	print(result)
#make_random_ints(5,1,13)

def make_random_ints_no_dupgs (num, lower_bound, upper_bound):
	result=[]
	rng =random.Random()
	for i in range (num):
		while True:
			candidate =rng.randrange(lower_bound,upper_bound)
			if candidate not in result:
				break
		result.append (candidate)
	return result
#xs = make_random_ints_no_dupgs(5,1,100)
#print(xs)


import time

def do_my_sum(xs):
    sum = 0
    for v in xs:
        sum += v
    return sum

sz=10000000
testdata=range(sz)

t0 =time.clock()
#my_result= do_my_sum(testdata)
t1=time.clock()
#print ("my result = {0}(time taken = {1:.4f} seconds)".format(my_result,t1-t0))


import seqtools
s = "A string!"
print (seqtools.remove_at(4,s))


n = 10
m = 3
def f(n):
   m = 7
   return 2*n+m
print(f(5), n, m)

#1
import calendar
cal = calendar.TextCalendar()
cal.setfirstweekday(3)
cal.prmonth(2012,8)

#7
def myreplace (old, new, s):
    x= s.split()
    new_list = []
    for i in x:
        if s == i:
            new_list.append(s)
        else:
            new_list.append(i)
    y="".join(new_list)
    print (y)
#myreplace (",", ";", "this, that, and some other thing")
