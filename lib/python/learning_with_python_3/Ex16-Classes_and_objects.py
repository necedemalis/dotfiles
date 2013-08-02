from unit_tester import test

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

class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__ (self,posn,w,h):
        self.corner = posn
        self.width = w
        self.height = h

    def __str__ (self):
        return "({0},{1},{2})".format(self.corner,self.width,self.height)

    def grow (self, delta_width, delta_height):
        self.width += delta.width
        self.height += delta.height

    def move (self, dx, dy):
        self.corner.x += dx
        self.corner.y += dy

    def area (self):
        return (self.width*self.height)

    def perimeter (self):
        return (self.width*2+self.height*2)

    def flip (self):
        a = self.height
        b = self.width
        self.width = a
        self.height = b

    def contains (self, p):
        if p.x >= self.width or p.y >= self.height:
            return False
        else:
            if p.x < self.corner.x or p.y < self.corner.y:
                return False
        return True

box = Rectangle(Point(0,0),100,200)
bomb = Rectangle(Point(100,80),5,10)
print ("box: ",box)
print ("bomb: ",bomb)

#16.4
import copy
p1 = Point(3,4)
p2 = copy.copy(p1)
print (p1 is p2)


#Exercises
#1
r = Rectangle(Point(0,0),10,5)
test (r.area()==50)

#2
test (r.perimeter()==30)

#3
r.flip()
test(r.width == 5 and r.height == 10)

#4
r = Rectangle(Point(0, 0), 10, 5)
test(r.contains(Point(0, 0)))
test(r.contains(Point(3, 3)))
test(not r.contains(Point(3, 7)))
test(not r.contains(Point(3, 5)))
test(r.contains(Point(3, 4.99999)))
test(not r.contains(Point(-3, -3)))

#5
def not_collide (r1, r2):
    r1w = r1.corner.x+ r1.width
    r2w = r2.corner.x+ r2.width
    r1h = r1.corner.y- r1.height
    r2h = r2.corner.y- r2.height
    if (r2h >= r1.corner.y or r2.corner.y <=r1h) and (r2.corner.x>= r1w or r2w <=r1.corner.x):
        return True
r= Rectangle(Point(0,2),3,2)
s= Rectangle(Point(3,4),5,3)
test (not_collide (r,s))

def is ()
    
