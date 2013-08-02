class MyTime:

    def __init__(self, hrs=0, mins=0, secs=0):
        """ Create a MyTime object initialized to hrs, mins, secs """
        totalsecs = hrs*3600 + mins*60  + secs
        self.hours = totalsecs // 3600
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60

    def __str__(self):
        return "({0}h {1}m {2}s)".format(self.hours, self.minutes, self.seconds)

    def to_seconds (self):
        return self.hours *3600 + self.minutes * 60 + self.seconds

    def after (self, time2):
        return self.to_seconds() > time2.to_seconds()

    def increment (self, seconds):
        inc = self.to_seconds() + seconds
        self.__init__ (0,0, inc)

    def between (self,t1,t2):
        if self.to_seconds() >= t1.to_seconds() and self.to_seconds() < t2.to_seconds():
            return True
        else:
            return False

    def __add__(self,other):
        return MyTime (0,0,self.to_seconds() + other.to_seconds())

    def __sub__(self,other):
        return MyTime (0,0,self.to_seconds() - other.to_seconds())

    def __gt__(self, time2):
        return self.to_seconds() > time2.to_seconds()


tim1 = MyTime (11,59,30)
tim1.increment (-60)
print(str(tim1))

t1 = MyTime(1, 15, 42)
t2 = MyTime(3, 50, 30)
t3 = t1 - t2
print(t3)


class Point:
    """ Create a new Point, at coordinates x, y """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other): #dot product
        return self.x * other.x + self.y * other.y

    def __rmul__(self, other): #scalar multiplication
        return Point(other * self.x,  other * self.y)



#Exercises
#2
t4 = MyTime(1,15,42)
print(t4.between(t1,t2))

#3
if t2 > t1:
    print("The bread will be done before it starts!")
