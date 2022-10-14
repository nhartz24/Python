# COMP112 F18
# Exam II Practice
# 2018-11-19 KMT
#

ans=True
question=0
questname=''


def nextquestion(prevquestnum,questname,exampart):
    # signature: str -> integer
    # prints out next question header with question# and name of question.
    # The current question number is returned to seed the next call.
    question=prevquestnum+1
    if exampart == 1:
        points=4
    elif exampart ==2:
        points=5
    elif exampart ==3:
        points=20
    else:
        print('This question was not found in any part of the exam.')
        return
    print('Question',str(question)+'. ',questname +'. (',points,'points).')
    return question


# Part I.  Closed Response Questions 4 points each *3 = 12 points


exampart=1


# True or False

question=nextquestion(question,'T or F',exampart)
print('In Python, len is overloaded to operate on dictionaries to return the \
number of keys plus values in the dictionary, similar to how it tells the \
number of items in a list.')

if ans==True:
    print('False.  Python is overloaded to operate on dicts but specifically \
reports the number of keys, not keys plus values, which will be double the \
number of keys.')


question=nextquestion(question,'Matching Constructs & IO',exampart)
# Match the following numbered items with the best letter choice(s):

#1. File IO
#2. Dictionaries
#3. Objects

#A. Allows one to compute a histogram
#B. Associates keys with values
#C. reading and writing information from a file
#D. Bundles variables and functions frequently used together

# Solution: (just for fun I will write it as a dictionary!)

soltn={'1':'C','2':['A','B'],'3':'D'}
print(soltn)


question=nextquestion(question,'Multiple Choice Method',exampart)
# A method can be called using ____.

#A. dot notation
#B. method syntax
#C. either dot notation or method syntax
#D. using the same syntax that is used to call functions.


print('C')


# Part II.  Short Answer. 8 questions * 6 points = 48 points
exampart=2

question=nextquestion(question,'Turtle Sketch',exampart)
print('In the space provided, draw the figure produced by the following \
program.  Assume that the canvas is initially blank and that the turtle \
starts at the center facing to the right.')
import turtle
turtle.forward (50)
turtle.left(45)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.left(45)
turtle.forward(50)


question=nextquestion(question,'Axes of Flight Keys',exampart)
axes=dict()
axes['x']='Longitudinal'
axes['y']='Lateral'
axes['z']='Vertical'
# Write a function to extract all the keys.

def extract_keys(mydict):
    # signature: dict -> list
    # extracts keys from dictionary
    
    acc=[]
    for key in mydict:
        #print(key)
        acc.append(key)
    return acc

# example of running it - not specifically required in the answer
print(extract_keys(axes))

question=nextquestion(question,'Axes of Flight values',exampart)
# Write a function to extract all the values

def extract_values(mydict):
    #signature: dict -> list
    # extracts values from dict

    return mydict.values()

# example of running it
print(extract_values(axes))


question=nextquestion(question,'Axes of flight search',exampart)
# write a function that searches all the values for a given input.


# the dictionary below associates the three axes of an airplane with
# a list containing the name of rotation about that axis as its 0th element,
# and the airfoil that controls it as the 1st element. 

steering=dict()
steering['x']=['roll','ailerons']
steering['y']=['pitch','elevators']
steering['z']=['yaw','rudder']

question=nextquestion(question,'Axes of flight listdict',exampart)
# write a function to return which axis a given airfoil controls.

# this is really not a short question because it is multistep.


def airfoil2axis(mydict,airfoil):
    #signature: dict -> list
    
#...make a new simpler dictionary
    newdict=()
    for key in mydict:
        afvalue=(mydict[key][1]) # pull out the 1th element of the list returned
        newdict[key]=afvalue # add to new, simple dictionary
#...use the simple dictionary to look up the info we want.Use reverse lookup.
    match_key=[]
    for key in newdict:
        if newdict[key]==airfoil:
            match_key.append(key)
    return match_key
            
        
        
#print(airfoil2axis(steering,'ailerons'))

question=nextquestion(question,'Axes of flight listdict execute',exampart)
# execute your function from the problem above and determine what the
# ailerons control. Print the result to the screen.



question=nextquestion(question,'Axes of flight compound functions',exampart)
# write a function to determine what airfoil
# controls longitudinal motion. Your function may call other functions you
# have created in the questions above.







question=nextquestion(question,'DirTree',exampart)
"""
         \
         | 
        Users
        /  |   \
   Ursula  Bob  Sunny
    /  \
MyDocs Music
  |       \
COMP_112   bach.mp3
 /   |  \
HW1 HW2 HW3
 |      | 
hw1.py  hw3.py
"""

print('Assume you are starting in the directory containng bach.mp3.  Write \
the code to navigate to COMP_112 and list all the files and directories \
that it contains.')







# Part III.  Code Writing 20 points each, 40 points total

exampart=3
question=nextquestion(question,'Circle',exampart)
print('A. Write a class called circle that will create an object circle. The circle \
should initialize with the given radius.  Printing the circle should \
report the radius.')

print('B. Write a method area for your circle class that will compute and return the\
area of the circle.  Recall from geometry that the formula for the area of a \
circle is: \
pi * radius squared.')

print('C. Create a specific circle circ with a radius of 7. Using your method \
from (B) above, compute the area of the circle and print out the value.')


print('D. Use looping to create circles c1 to c5, having radii of integer values \
#1 to 5.  Collect the areas of these circles in a list.')

import math
#A.
class circle(object):
    def __init__(self,radius=1):
        self.radius=radius
    def __str__(self):
        return('radius='+str(self.radius))    
#B.
    def area(self):
        A = math.pi * self.radius * self.radius
        return A
#C. make an instance of a circle with radius 7 and compute area
circ=circle(7)
print(circ)
print(circle.area(circ))
"""
radius=7
153.93804002589985
"""

#D.
areas=[]
for i in range (1,6):
    print(i)
    cname='circle'+str(i)
    print (cname)
#...instantiation
    cname=circle(i)
#...compute the area
    A=circle.area(cname)
#...append the current area to the growing list
    areas.append(A)

print ("The circle areas are:\n",areas)


question=nextquestion(question,'Histogram',exampart)

# A survey was given to students to select the number corresponding
# to their favorite place to study. THe options were:
# 1. outside
# 2. Olin
# 3. SciLi
# 4. dorm room
# 5. Other

# The results are in!  The data collected so far are compiled in a list.

#A. write a dictionary mapping the survey choice number to the favorite
# study location.


#B. Write a dictionary that will take a list as input and tally the
# results.  Write a print statement that reports the most popular
# study location.



def histdat(data):
    dictdat={}
    for pt in data:
        if pt not in dictdat:
            dictdat[pt]=1
        else:
            dictdat[pt]+=1
    return dictdat


data = [5, 3, 4, 5, 4, 3, 4, 3, 2, 5]
Ans=histdat(data)
print(Ans)









