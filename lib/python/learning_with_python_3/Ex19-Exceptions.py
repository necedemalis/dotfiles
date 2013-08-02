    age = int(input("Please enter your age: "))
    if age < 0:
        # Create a new instance of an exception
        my_error = ValueError("{0} is not a valid age".format(age))
        raise my_error
    return age

#get_age()


def recursion_depth(number):
    print("Recursion depth number", number)
    try:
        recursion_depth(number + 1)
    except:
        print ("I cannot go any deeper!")

#recursion_depth(0)


import turtle
import time
def show_poly():
    try:
        win = turtle.Screen()
        tess = turtle.Turtle()

        n = int(input("How many sides?"))
        angle = 360 / n
        for i in range (n):
            tess.forward(10)
            tess.left(angle)
        time.sleep(3)
    finally:
        win.bye()

#show_poly()


#1
def inp_int (i):
    try:
        number = int((input("Geben sie eine ganze Zahl ein: ")))
    except:
        print ("Ihre Eingabe ",number," enspricht nicht den Voraussetzungen.")
    print (number)

inp_int(5)

