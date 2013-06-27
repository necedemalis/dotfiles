class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0,y=0):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """Compute my distance from the origin """
        return ((self.x **2) + (self.y **2)) ** 0.5

    def __str__ (self):
        return "({0},{1})".format(self.x,self.y)

    def halfway (self, target):
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx,my)

    def reflect_x (self):
        return (self.x, -(self.y))

    def slope_from_origin(self):
        return (self.y/self.x)

    def get_line_to (self, target):
        a = (target.y - self.y)/(target.x - self.x)
        b = self.y-self.x*2
        return (int(a),b)

p = Point(3,4)
q = Point(5,12)
print (p.x,p.y,q.x,q.y)
print (p.distance_from_origin())
print(p)

def midpoint (p1,p2):
    mx = (p1.x + p2.x)/2
    my = (p1.y + p2.y)/2
    print (Point(mx,my))
#midpoint(p,q)

print (p.halfway(q))


#Exercises#
#Ex1
def distance (p1,p2):
    dx = p2.x - p1.x
    dy = p2.y - p2.y
    result = (dx+dy)**0.5
    return result
print (distance (p,q,))

#Ex2
print (Point(3,5).reflect_x())

#Ex3
print (Point(4,10).slope_from_origin())

#Ex4
print (Point(4,11).get_line_to(Point(6,15)))

#Ex5
class SMS_store:
    """ SMS class will store messages """

    def __init__ (self):
        self.x = []

    def __str__ (self):
        return ("{0}".format(self.x))

    def add_new_arrival(self, x,y,z):
        self.x.append ([False,x,float(y),z],)
    
    def message_count(self):
        return len(self.x)

    def get_unread_indexes(self):
        nonread=[]
        for i in self.x:
            if i[0] == False:
                nonread.append(i[1:])
        return nonread

    def get_messages(self,p):
        a = self.x[p]
        a[0] = True
        self.x[p] = a
        return a[1:]

    def delete(self,i):
        del self.x[i]

    def clear (self):
        self.x=[]

my_inbox = SMS_store ()

#a
my_inbox.add_new_arrival (50394, 15, "Hallo Welt")
my_inbox.add_new_arrival (402193, 16.10, "Hallo Echo")
my_inbox.add_new_arrival (999999, 17.10, "Hallo Otto")

#b
print (my_inbox.message_count())

#d
print (my_inbox.get_messages(1)) 

#c
print (my_inbox.get_unread_indexes())

#e
my_inbox.delete(1)
print (my_inbox)

#d
my_inbox.clear()
print (my_inbox)

