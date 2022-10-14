# 1 --> True

# 2  1 --> C
#    2 --> A, B
#    3 --> D

# 3 --> C

# 4                  /\
#                   /  \
#                  /    \
#                 /      \
#                /        \
#           -----          -----

'''
# 5

axes=dict()
axes['x']='Longitudinal'
axes['y']='Lateral'
axes['z']='Vertical'

def extract_keys():
    x  = axes.keys()
    return x

# 6
def extract_vals():
    return axes.values()

# 7

def search(x):
    acc = []
    for char in axes.values():
        if char == x:
            acc.append(char)
    return acc


# 8 

steering=dict()
steering['x']=['roll','ailerons']
steering['y']=['pitch','elevators']
steering['z']=['yaw','rudder']

def control(given,airfoil):
    mydict = {}
    acc = []
    for char in given:
        mydict[char] = given[char] [1]
        
    for char in mydict:
        if mydict[char] == airfoil:
            acc.append(char)
    return acc


# 10

def longitude(given):
    mydict = {}
    acc = []
    for char in given:
        mydict[char] = given[char]
        
    for char in mydict:
        if char == 'x':
            acc.append(mydict[char])
    return acc


# 11
import os

os.getcwd()
os.chdir('../MyDocs/Comp_112')
os.listdir()

# 12
import math
class Circle:

    def __init__(self,radius):
        self.radius = radius

    def __str__(self):
        radius = ('The radius is ' + str(self.radius))
        return radius

    def area(self):
        A = (math.pi * self.radius * self.radius)
        return A


circ = Circle(7)
c = circ.area()
print(c)



def circles():
    acc = []
    for i in range (1,6):
        print(i)
        cname = 'c'+str(i)
        print(cname)
        cname = Circle(i)
        A = cname.area()
        acc.append(A)
    return acc
        


study = {1: 'outside', 2: 'Olin', 3: 'SciLi', 4: 'dorm room', 5: 'Other'}


def popular(x):
    mydict = {}
    for char in x:
        if char not in mydict:
            mydict[char] = 1
        else:
            mydict[char] += 1

    print(mydict)



# 5

axes=dict()
axes['x']='Longitudinal'
axes['y']='Lateral'
axes['z']='Vertical'

def extract_keys():
    # sig nonetype --> list[str]
    # Writes a function to extract all the keys in axes

    return axes.keys()

def extract_vals():
    # sig nonetype --> list[str]
    # Writes a function to extract all the values in axes

    return axes.values()

def search(axes,x):
    # sig str --> str
    #  searches all the values for a given input specified by the user
    acc = []
    val = axes.values()
    for value in val:
        if val == x:
            acc.append(value)
    for key in axes:
        if axes[key] in acc:
            return key
            


steering=dict()
steering['x']=['roll','ailerons']
steering['y']=['pitch','elevators']
steering['z']=['yaw','rudder'] 
def control(steering,airfoil):
    # sig dict{str} --> str
    #  returns which axis a given airfoil controls
    simpdict = {}
    for key in steering:
        simpdict[key] = steering[key] [1]
    for key in simpdict:
        if airfoil in simpdict[key]:
            return key

# 10

def longitude(steering):
    # sig dict{str} --> str
    # determinse what airfoil controls longitudinal motion
    acc = []
    for key in axes:
        if 'Longitudinal' in axes[key]:
            acc.append(key)
    
    for char in acc:
        return steering[char] [1]


# 11

import os
os.getcwd()
os.chdir("../Ursula/MyDocs/Comp_112")
os.listdir()

# 12
import math
class circle:

    def __init__(self,radius):
        # sig int/float ---> nonetype
        # initializes variable radius 

        self.radius = radius

        
    def __str__(self):
        # sig nonetype --> str
        # prints the radius when circle is called 
        return ('your radius is' + str(self.radius))

    def area(self):
        # sig nonetype --> float
        # returns area of a specific circle

        return (math.pi * self.radius * self.radius)

circ = circle(7)
A = circ.area()
print(A)


def loop():
    acc = []
    for i in range (1,6):
        c = circle(i)
        acc.append(c.area())
    return acc
        

study = {1: 'outside', 2: 'Olin', 3: 'SciLi', 4: 'dorm room', 5: 'other'}
data = [5, 3, 4, 5, 4, 3, 4, 3, 2, 5]

def popular(x):
    # sig list[int] --> dict{int}
    #  Writes a function that will take a list as input and tally the results
    mydict = {}
    for char in x:
        if char not in mydict:
            mydict[char] = 1
        else:
            mydict[char] += 1
    return mydict

a = popular(data)
print(a)
'''

axes=dict()
axes['x']='Longitudinal'
axes['y']='Lateral'
axes['z']='Vertical'


def search(axes,x):
    val = axes.values()
    acc = []
    for value in val:
        if x in value:
            acc.append(value)

    for key in axes:
        if axes[key] in acc:
            return key

steering=dict()
steering['x']=['roll','ailerons']
steering['y']=['pitch','elevators']
steering['z']=['yaw','rudder']




    
import os
def trial():
    s = open("trial.txt", "r")
    for line in s:
        print(line)
    s.close()
        















    
    
