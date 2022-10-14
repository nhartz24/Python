# Kelly M. Thayer
# 2020-02-02
# COMP112-01&02
# Lab 2 week 3 Variables, Statements, and Expressions
# Solutions
#

#Question 1
""">>> 2+3
5
>>> type(2+3)
<class 'int'>
>>> 1-5.2
-4.2
>>> type(1.-52)
<class 'float'>
>>> 4*2
8
>>> type(4*2)
<class 'int'>
>>> 3**2
9
>>> type(3**2)
<class 'int'>
>>> 12/6
2.0
>>> type(12/6)
<class 'float'>
>>> 59/60
0.9833333333333333
>>> type(59//60)
<class 'int'>"""
# Question 2
"""2+3 will yield an int whereas 2.0+3 will yield a float."""
# Question 3
""" >>> 1,000+3
(1, 3)
It behaves as a tuple, which the students haven't learned yet.
The point is, don't use commas because it won't do what you think it will. """
# Question 4
""">>> 3+a
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    3+a
NameError: name 'a' is not defined
you can not add a letter to a number; you could however make it a variable."""
# Question 5
""">>> 3*5+5*6
45
>>> 1+2+3+4
10
>>> 8+4*3+2
22
>>> 
Yes, they all follow the order of operations."""
# Question 6
"""
>>> type('Hello world!')
<class 'str'>
>>> type('first_name')
<class 'str'>
>>> type('71')
<class 'str'> """
#Question 7
"""71 is an integer.  71.0 is a float.  '71' is a string."""
#Question 8
"""
>>> pi = 22/7
>>> r = 2
>>> C = 2 * pi * r
>>> C
12.571428571428571"""
#Question 9
"""
>>> l = 4
>>> w = 8
>>> h = 10
>>> V = l * w * h
>>> V
320"""
#Question 10
""" if V were typed before h were assigned, an error would occur
because h would have no value and therefore the V could not be
computed."""
#Question 11.
"""
>>> w=16
>>> V=l*w*h #do not forget to reassign the variable
>>> V
640"""
# Question 12.
"""
var_name(?)    Valid(Y/N)    If not, why?
volume          Y
3Sides          N            Do not begin with a number
side3           Y
friend_Name     Y
friendName      Y
averyververyveryloooooongname Y
finally@        N           do not use special characters such as @
int             N           do not use build in python words """
# Question 13.
"""
>>> print(shape*3)
cubecubecube
>>> shape='square'
>>> print(shape**2)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    print(shape**2)
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
>>> 
squaring a word is not defined in python."""
# Question 14.
"""WHen there is no print statement, the script file will not report
the value of the variable. Modify the script to print your variable."""

#------------------PROBLEMS--------------------------------------------

# Lab 2 Exercise 1 Program Volume

# small box
l = 8.5
w = 5.5
h = 1.5
V = l*w*h
ppuv= 6.80/V # price per unit volume
print('SMALL BOX')
print('Volume of box is:')
print(V)
print('Price per unit volume:')
print(ppuv)

# medium box type 1
l = 11.0
w = 8.5
h = 5.5
V = l*w*h
ppuv= 13.45/V # price per unit volume
print('MEDIUM TYPE 1 BOX')
print('Volume of box is:')
print(V)
print('Price per unit volume:')
print(ppuv)

# medium box type 2
l = 13.5
w = 12
h = 3.5
V = l*w*h
ppuv= 13.45/V # price per unit volume
print('MEDIUM TYPE 2 BOX')
print('Volume of box is:')
print(V)
print('Price per unit volume:')
print(ppuv)

# large box
l = 12
w = 12
h = 5.5
V = l*w*h
ppuv= 18.75/V # price per unit volume
print('LARGE BOX')
print('Volume of box is:')
print(V)
print('Price per unit volume:')
print(ppuv)

"""
SMALL BOX
Volume of box is:
70.125
Price per unit volume:
0.09696969696969697
MEDIUM TYPE 1 BOX
Volume of box is:
514.25
Price per unit volume:
0.02615459406903257
MEDIUM TYPE 2 BOX
Volume of box is:
567.0
Price per unit volume:
0.023721340388007054
LARGE BOX
Volume of box is:
792.0
Price per unit volume:
0.023674242424242424
The price per unit volume is the smallest for the large box
"""
print('The price per unit volume is the smallest for the large box')



# Lab 2 Exercise 2
# This program calculates the volume of a sphere

#A. Earth
pi=22/7
r=3959
V=(4/3)*pi*r**3
print('The volume of Earth is:')
print(V)

#B. Soccer Ball
r=11
V=(4/3)*pi*r**3
print('The volume of a soccer ball is:')
print(V)

#C. carbon atom
r=170
V=(4/3)*pi*r**3
print('The volume of a carbon atom is:')
print(V)

# notice that they all use very different scales of measure.




