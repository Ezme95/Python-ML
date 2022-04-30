# if statements
x = 5
if x < 6:
    print ("Smaller")
if x > 6:
    print ("Bigger")


#if else statements
# for functions, place ":" at the end, next line is the actions of the function

print ("Finish")
if x == 5 :
    print("oh no its 5")
else :
    print("oh yes, its not five")


# assigning functions to variable;
def greet():
    # used end= in previous line to print next in same line
    """indentation in python refers to a block of code; not just for readability like
    in other programs"""
    print("hello", end='')

x = input ("Enter your name")
greet(); print (x)

# Many values to multiple variables
x,y,z = "Orange", "Banana", "Cherry"
print (x, end=' ')
# end= ' ' print in same line
print (y, end =' ')
print (z)

# one value to multiple variables
x = y = z = "Orange"
print (x, end=' ')
# end= ' ' print in same line
print (y, end =' ')
print (z)

# global variable, where variable operates outside of the local function

# create variable outside of the function (global)
x = "awesome"

# initiate variable inside function
def myFunc() :
    x = "fantastic"
    print ("Python is " + x)

# call function, prints internal variable
myFunc()

# calls global variable
print("Python is " +  x)

# use global keyword changes the variable scope to global
def myFunc() :  # define function
    global x
    x = "fabulous"

myFunc() # call function

print(x) # print variable

# random numbers

import random
print(random.randrange(1,10))

# upp
