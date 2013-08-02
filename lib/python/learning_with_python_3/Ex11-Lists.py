xs = [1, 2, 3, 4, 5]
#print(xs[1])

for (i, val) in enumerate(xs):
    xs[i] = val**2
#print (xs)

for (i, v) in enumerate(["banana", "apple", "pear", "lemon"]):
     print(i, v)

def double_stuff(a_list):
	""" Overwrite each element in a_list with double its value. """

	for (idx, val) in enumerate(a_list):
		a_list[idx] = 2 * val
things = [2, 5, 9]
double_stuff(things)
#print(things)

def double_stuff2(a_list):
    """ Return a new list which contains
        doubles of the elements in a_list.
    """
    new_list = []
    for value in a_list:
        new_elem = 2 * value
        new_list.append(new_elem)

    return new_list

#5
def add_vectores(u,v):
	count=0
	new_list=[]
	for x in u:
		a= u[count]+v[count]
		new_list.append (a)
		count +=1
	return new_list
#print(add_vectores([1, 2, 1], [1, 4, 3]))

#6
def scalar_mult(s,v):
	new_list=[]
	for x in v:
		a= x*s
		new_list.append(a)
	return new_list
#print(scalar_mult(7, [3, 0, 5, 11, 2]))

#7
def dot_product (u,v):
	new_list=[]
	res=0
	for (pos,val) in enumerate(u):
		a= val*v[pos]
		res= res+a
	return res
#print (dot_product([1, 2, 1], [1, 4, 3]))

#8
#def cross_product(u,v):
#	new_list []
#	for (pos, val) in enumerate(u):
#		a=val*v[pos+1] - val

#9
def replace (s,old,new):
	st= s.split(old)
	return new.join (st)
#print (replace ("I love spom! Spom is my favorite food. Spom, spom, yum!", "om", "am"))


