import sys

def test(did_pass):


    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def turn_clockwise (n):
    if n == "N":
        return "E"
    elif n == "E":
        return "S"
    elif n == "S":
        return "W"
    elif n == "W":
        return "N"







def day_name(n):
    if n==0:
        return "Sunday"
    elif n==1:
        return "Monday"
    elif n==2:
        return "Tuesday"
    elif n==3:
        return "Wednesday"
    elif n==4:
        return "Thursday"
    elif n==5:
        return "Friday"
    elif n==6:
        return "Saturday"
    else:
        return None

def day_num(n):
    if n=="Sunday":
        return 0
    elif n=="Monday":
        return 1
    elif n=="Tuesday":
        return 2
    elif n=="Wednesday":
        return 3
    elif n=="Thursday":
        return 4
    elif n=="Friday":
        return 5
    elif n=="Saturday":
        return 6
    else:
        return None

def day_add (x,y):
    a=day_num(x)
    b=a+y
    if b < 0:
        b=b+7
        b= abs(b)
    if b > 6:
        b= b%7
    c= (day_name(b))
    return c


def to_secs (h,m,s):
    a=h*60
    b=(m+a)*60
    c=s+b
    return int(c)


def minutes_in (x):
    m=int(x/60)
    a=m%60
    return a



def hypotenuse (x,y):
    return (x**2+y**2)**0.5

def ack (m,n):
    if m == 0:
        return n+1
    elif (m>0)and(n==0):
        return ack (m-1,1)
    elif (m>0)and(n>0):
        return (ack (m-1,(ack(m,n-1))))

##Anderes Tutorial
def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]
def is_palindrome(word):
    """Returns True if word is a palindrome."""
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))


def is_power (a,b):
    if (((a%b) == 0) and (a!=b)):
        return (is_power (a/b,b))
    elif (a==b):
        return True
    elif (a!=b):
        return False 

def gcd (a,b):
    if (a%b==0):
        return b
    elif (a%b==1):
        return 1
    elif (a%b > 1):
        return gcd (b,a%b)

print (day_add("Sunday", -574564))


#Test-Suite
def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(turn_clockwise("N") == "E")
    test(turn_clockwise("W") == "N")
    test(day_name(3) == "Wednesday")
    test(day_name(6) == "Saturday")
    test(day_name(42) == None)
    test(day_num("Friday") == 5)
    test(day_num("Sunday") == 0)
    test(day_num(day_name(3)) == 3)
    test(day_add("Monday", 4) ==  "Friday")
    test(day_add("Tuesday", 0) == "Tuesday")
    test(day_add("Tuesday", 14) == "Tuesday")
    test(day_add("Sunday", 100) == "Tuesday")
    test(day_add("Sunday", -1) == "Saturday")
    test(day_add("Sunday", -7) == "Sunday")
    test(day_add("Tuesday", -100) == "Sunday")
    test(to_secs(2, 30, 10) == 9010)
    test(to_secs(2, 0, 0) == 7200)
    test(to_secs(0, 2, 0) == 120)
    test(to_secs(0, 0, 42) == 42)
    test(to_secs(0, -10, 10) == -590)
    test(to_secs(2.5, 0, 10.71) == 9010)
    test(to_secs(2.433,0,0) == 8758)
    test(minutes_in(9010) == 30)
    test(hypotenuse(3, 4) == 5.0)

test_suite()






