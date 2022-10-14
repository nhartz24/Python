# Noah Hartzfeld
# Section 5
#10/06/2020

import turtle

# Question 1
'''
turtle.forward(100)
turtle.left(90)
turtle.forward(50)
turtle.left(45)
turtle.back(100)
turtle.clear
'''
# Question 2
'''
turtle.bgcolor("pink")
turtle.color ("green")
turtle.pensize(10)
turtle.forward(20)
turtle.reset()
'''

# Question 3
def mystery (size):
    i = 0
    while i < 4:
        turtle . forward(size)
        turtle . right(90)
        i = i + 1
# it will print a square

'''
A. Size describes the length of each line it is signifigant to make sure they are all the same

B. The 4 is significant because it makes sure that 4 sides are printed

C. The 90 degree right function call means the next line drawn will be perpendicular to the last

D. '''
for i in range (18):
    mystery(100)
    turtle . right (20)


