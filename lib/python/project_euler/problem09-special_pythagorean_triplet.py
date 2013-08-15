from itertools import combinations

def pythagorean_triplets():
    '''Find the one Pythagorean triplet for which a + b + c = 1000. Find the product abc.'''
    tuple_list = combinations(range(1,24),2)
    triplet_sum = 0
    for tup in tuple_list:
        (v,u)=tup
        x=u**2-v**2 #Formel um pythagoreische Tripel zu erzeugen.
        y=2*u*v
        z=u**2+v**2
        triplet_sum = x+y+z
        if triplet_sum == 1000:
            print ("{}+{}+{} = {}".format(x,y,z,(x+y+z)))
            print ("{}*{}*{} = {}".format(x,y,z,(x*y*z)))

from datetime import datetime
now = datetime.now()
pythagorean_triplets()
print(datetime.now()-now)
