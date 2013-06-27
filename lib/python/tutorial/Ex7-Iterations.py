
def test(did_pass):
    import sys
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def mysum (xs):
    running_total = 0
    for x in xs:
        running_total=running_total+x
    return running_total
    
def sum_to(n):
    """ Return the sum of 1+2+3 ... n """
    ss  = 0
    v = 1
    while v <= n:
        ss = ss + v
        v = v + 1
    return ss
def sum_to2(n):
    """ Return the sum of 1+2+3 ... n """
    ss  = 0
    n=n+1
    for v in range(n):
        ss = ss + v
    return ss




def seq3np1 (n):
    while n !=1:
            print (n, end=" , ")
            if n%2==0:
                n=n//2
            else:
                n=n*3+1
    print (n, end=".\n")


def num_digits (n):
    count = 0
    if n==0:
        return 1
    else:
        while n !=0:
            count=count+1
            n=abs(n)//10
        return count
#print (num_digits(-24676))



def print_multiples(n,t):
    for i in range(1, t+1):
            print(n * i, end="    ")
    print()

def print_mult_table(t):
    for i in range (1,t+1):
        print_multiples(i,t)
#print (print_mult_table (150))

def guess_nbr():
    import random
    rng = random.Random()
    number= rng.randrange(1,1000)
    guesses=0
    msg =""
    
    while True:
        guess=int(input(msg+"\nGuess my number between 1 and 1000: "))
        guesses+=1
        if guess > number:
            msg += str(guess)+" is too high.\n"
        elif guess < number:
            msg += str(guess)+" is too low.\n"
        else:
            break
    input("\n\nGreat, you got it in {0} guesses!\n\n".format(guesses))
#guess_nbr()



def no_odds():
    for i in [12, 16, 17, 24, 29, 30]:
        if i % 2 == 1:      # If the number is odd
           continue         # Don't process it
        print(i)
    print("done")


def celebs ():
    celebs = [("Brad Pitt", 1963), ("Jack Nicholson", 1937), 
    ("Justin Bieber", 1994)]

    for (nm, yr) in celebs:
        if yr < 1980:
            print (nm)

def students ():
    students = [
    ("John", ["CompSci", "Physics"]),
    ("Vusi", ["Maths", "CompSci", "Stats"]),
    ("Jess", ["CompSci", "Accounting", "Economics", "Management"]),
    ("Sarah", ["InfSys", "Accounting", "Economics", "CommLaw"]),
    ("Zuki", ["Sociology", "Economics", "Law", "Stats", "Music"])]

    for (name, subjects) in students:
        print (name, "takes", len(subjects), "courses.\n")
    
    counter=0
    for (name, subjects) in students:
        for s in subjects:
            if s == "CompSci":
                counter+=1
    print ("The number of studens taking CompSci is", counter)



def sqrt (n):
    approx=n/2.0
    while True:
        better = (approx+n/approx)/2.0
        if abs (approx-better)<0.001:
            return better
        approx = better
    # print (sqrt(25))

##Exercises#################

#1
def how_many_odds (n):
    count =0
    for i in (n):
        if (i%2)==1:
            count +=1
    print (count, "ungerade Zahlen.")
#print (how_many_odds ([3,7,5,9,43,8,1,6]))

#2
def sum_up_evens (n):
    count=0
    for i in (n):
        if (i%2)==0:
            count += i
    print (count)
#print (sum_up_evens ([3,7,5,9,43,8,1,6]))

#4
def word_length (n):
    count=0
    for i in (n):
        if (len(i))==5:
            count +=1
    print (count)
#print (word_length(["Peter", "Paul", "Mary", "Josef"]))
#5
def first_even (n):
        for i in (n):
            if i%2==1:
                print (i)
            else:
                break
#print (first_even([5,7,9,2,4,13]))

#6
def first_sam (n):
    count=0
    for i in (n):
        if i != "sam":
            count +=1
        else:
            count +=1
            break
    print (count)
#print(first_sam(["peter","paul","sam","mary", "robert"]))


#7
def sqrt2 (n):


    approx=n/2
    while True:
        better = (approx+n/approx)/2.0
        if abs (approx-better)>=0.001: 
            print (better)
        else:
            return better
        approx = better
#print (sqrt2(16))




#9
def print_triangular_number(n):
    count=0
    nummer=1
    for i in range (1,n+1):
        count += i
        print (nummer, "    ", count)
        nummer +=1
    print ()
#print (print_triangular_number(5))

#10
def is_prime (n):
    for i in range (2,n):
        if n%i==0:
            return False
        else:
            return True
print(is_prime(11))

#11

#11
def drunk_turtle (n):
    import turtle
    wn=turtle.Screen()
    wn.bgcolor("lightgreen") 
    wn.title("Hello, Tess!")      # Set the window title
    
    tess = turtle.Turtle()
    tess.color("blue")            # Tell tess to change her color
    tess.pensize(3)               # Tell tess to set her pen width
    
    for (i,j) in (n):
        tess.left (i);
        tess.forward(j)
    
    wn.mainloop()
#print (drunk_turtle ([(160, 20), (-43, 10), (270, 8), (-43, 12)]))


#12
def nikolaus_haus ():
    import turtle
    wn=turtle.Screen()
    wn.bgcolor("lightgreen") 
    wn.title("Das ist das Haus des Nikolaus")      # Set the window title
    
    tess = turtle.Turtle()
    tess.color("blue")            # Tell tess to change her color
    tess.pensize(3)               # Tell tess to set her pen width

    count=0
    while count < 3:
        tess.forward (100);
        if count==0:
            tess.left (135)
        elif count==2:
            tess.left (-45)
        else:
            tess.left (-135)
        if count==2:
            tess.forward ((((100**2)*2)**0.5)/2);
        else:
            tess.forward (((100**2)*2)**0.5);
        if count==2:
            tess.left (-90)
            tess.forward ((((100**2)*2)**0.5)/2);
            tess.left (-45)
            tess.forward(100)
        else:
            tess.left (-135)
        count +=1
    wn.mainloop()
nikolaus_haus()

#16
def sum_of_squares(xs):
    num=0
    for i in (xs):
        num=num+i**2
    print (num)
#print (sum_of_squares([2, 3, 4]))

#Est. Pi
def factorial (n):
    sum=n
    if n ==0:
        return 1
    else:
        while n !=1:
            sum=sum*(n-1)
            n -=1
    return sum
#print (factorial (5))
def estimate_pi ():
    total =0
    k=3
    while True:
        factor= (2*(2**0.5))/9801
        num= (factorial(4*k))*(1103+26390*k)
        den=((factorial(k))**4)*(396**(4*k))
        term=factor*(num/den)
        total +=term
        if abs(total) <1e-15:
            break
        else: 
            k +=1
    print (1/total)
#estimate_pi()



def test_suite():
    test(sum_to2(4) == 10)
    test(sum_to2(1000) == 500500)
#test_suite ()

