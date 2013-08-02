import turtle
import os
#import pygame
import math
from unit_tester import test


#18.1
def koch (t,order,size):
    if order == 0:
        t.forward (size)
    else:
        for angle in [60,-120,60,0]:
            koch (t,order-1, size/3)
            t.left(angle)
#wn = turtle.Screen()
#t = turtle.Turtle()
#koch (t, 1, 100)
#raw_input()
#wn.mainloop


#18.3
def r_sum (nested_num_list):
    tot = 0
    for element in nested_num_list:
        if type(element) == type([]):
            tot += r_sum(element)
        else:
            tot += element
    return tot

def r_max (nxs):
    largest = None
    first_time = True
    for e in nxs:
        if type(e) == type([]):
            val = r_max(e)
        else:
            val = e

        if first_time or val > largest:
            largest = val
            first_time = False

    return largest
test(r_max([2, 9, [1, 13], 8, 6]) == 13)
test(r_max([2, [[100, 7], 90], [1, 13], 8, 6]) == 100)
test(r_max([[[13, 7], 90], 2, [1, 100], 8, 6]) == 100)
test(r_max(["joe", ["sam", "ben"]]) == "sam")


#18.4
def fib(n):
    if n <= 1:
        return n
    t = fib(n-1) + fib(n-2)
    return t

#18.5
def get_dirlist(path):
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist

def print_files(path, prefix = ""):
    if prefix == "":
        print ("Folder listing for", path)
        prefix = "|"

    dirlist = get_dirlist (path)
    for f in dirlist:
        print (prefix + f)
        fullname = os.path.join(path, f)
        if os.path.isdir (fullname):
            print_files (fullname, prefix + "| ")
#print_files("/home/joecool/lib")


#18.6
#pygame.init()

# Create a new surface and window.
surface_size = 1024
#main_surface = pygame.display.set_mode((surface_size,surface_size))
#my_clock = pygame.time.Clock()

def draw_tree(order, theta, sz, posn, heading, color=(0,0,0), depth=0):

   trunk_ratio = 0.29       # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_x = trunk * math.cos(heading)
   delta_y = trunk * math.sin(heading)
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   pygame.draw.line(main_surface, color, posn, newpos)

   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
      if depth == 0:
          color1 = (255, 0, 0)
          color2 = (0, 0, 255)
      else:
          color1 = color
          color2 = color

      # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree(order-1, theta, newsz, newpos, heading-theta, color1, depth+1)
      draw_tree(order-1, theta, newsz, newpos, heading+theta, color2, depth+1)

def gameloop():

    theta = 0
    while True:

        # Handle evente from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break;

        # Updates - change the angle
        theta += 0.01

        # Draw everything
        main_surface.fill((255, 255, 0))
        draw_tree(9, theta, surface_size*0.9, (surface_size//2, surface_size-50), -math.pi/2)

        pygame.display.flip()
        my_clock.tick(120)
#gameloop()
#pygame.quit()



#Exercises
#1
def koch2 (order,size):
    for i in range (3):
        koch (t, order,size)
        t.right (120)
wn = turtle.Screen ()
t = turtle.Turtle()
koch2 (5, 100)
raw_input()
wn.mainloop()

#2
def cesaro (t,order,size):
    if order == 0:
        t.forward (size)
    else:
        for angle in [-85,170,-85,0]:
            cesaro (t,order-1,size/3)
            t.left (angle)

def cesaro_sqr (order,size):
    for i in range (4):
        cesaro (t,order,size)
        t.right (90)
#wn = turtle.Screen ()
#t = turtle.Turtle()
#cesaro_sqr (5, 1500)
#wn.mainloop()

#3
def sierpinski (t,order,size,colorChangeDepth, c=0):
    if order == 0:
        for i in range (3):
            t.forward (size)
            t.left (120)
    else:
        for i in range (3):
            sierpinski(t,order-1,size/2, colorChangeDepth)
            t.forward (size)
            t.left (120)
            if colorChangeDepth > -1 :
                if order >= colorChangeDepth:
                    if c <=1:
                        c +=1
                    else:
                        c ==0
                    colors = ["red","blue","magenta"]
                    t.color(colors[c])
#wn = turtle.Screen ()
#t = turtle.Turtle()
#t.color ("red")
#sierpinski(t,3,100, 2)
#wn.mainloop()

#5
def recursive_min (nxs):
    largest = None
    first_time = True
    for e in nxs:
        if type(e) == type([]):
            val = recursive_min(e)
        else:
            val = e

        if first_time or val < largest:
            largest = val
            first_time = False

    return largest
test(recursive_min([2, 9, [1, 13], 8, 6]) == 1)
test(recursive_min([2, [[100, 1], 90], [10, 13], 8, 6]) == 1)
test(recursive_min([2, [[13, -7], 90], [1, 100], 8, 6]) == -7)
test(recursive_min([[[-13, 7], 90], 2, [1, 100], 8, 6]) == -13)

#7
def flatten (nxs):
    new_list = []
    for i in nxs:
        if type(i).__name__ == "list":
            in_list = flatten (i)
            new_list.extend(in_list)
        else:
            new_list.append(i)
    return new_list
test(flatten([2,9,[2,1,13,2],8,[2,6]]) == [2,9,2,1,13,2,8,2,6])
test(flatten([[9,[7,1,13,2],8],[7,6]]) == [9,7,1,13,2,8,7,6])
test(flatten([[9,[7,1,13,2],8],[2,6]]) == [9,7,1,13,2,8,2,6])
test(flatten([["this",["a",["thing"],"a"],"is"],["a","easy"]]) ==
              ["this","a","thing","a","is","a","easy"])
test(flatten([]) == [])

#8
def fib2 (n):
    if n <= 1:
        return n
    fib2 = 0
    fib1 = 1
    counter = 1
    while counter < n:
        number = fib1 +fib2
        fib2 = fib1
        fib1 = number
        counter += 1
    return number
#print (fib2(7))

#9
def dir_str (path):
    dirlist = get_dirlist (path)
    for f in dirlist:
        new_path = os.path.join (path, f)
        if os.path.isfile(new_path):
            print (new_path)
        elif os.path.isdir (new_path):
            dir_str (new_path)

#dir_str("/home/joecool")

