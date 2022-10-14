# Noah Hartzfeld
# Section 5
# 11/19/2020
import os


# Quesion 1

#True



# Question 2
# True



# Question 3
# False


# Question 4

# False


# Question 5

# D


# Question 6
#B

# Question 7

#D

# Question 8

# SKIP

# Question 9
d = {1: 'A', 2: 'B', 3: 'C'}

d = dict()

d[1] = 'A'
d[2] = 'B'
d[3] = 'C'

alpha = ['A','B','C']
def loop(alpha):
    # sig list[str] --> dict[str]
    # makes a dict mapping letter of the alphabet to their coresponding place
    d = {}
    z = 0
    for i in range(1,4):
        d[i] =  alpha[z]
        z += 1
    return d
    

# Question 10

# SKIP

# Question 11
L1=['Orleans','Yarmouth','Dennis','Harwich','Chatham']
L2=[75, 25, 20, 33, 40 ]

def dist2town(L1,L2):
    # sig list[str],list[int] --> dict{int:str}
    # returns a dictionary mapping the distance from the bridge to the name of the town
    
    mydict = {}
    i = 0
    for char in L2:
        mydict[char] = L1[i]
        i += 1
    return mydict
        


# Question 12
def order(L2):
    # sig list[int]-> list[str]
    # returns a list ordering the towns closest to furthest from the bridge 
    mydict = dist2town(L1,L2)
    acc = []
    for char in sorted(L2)
        acc.append(mydict[char])


# Question 13
os.chdir('../../covid_19/Theodor')

os.chdir('/home33/covid_19/Theodore')

# Question 14

# SKIP


# Question 15

# A --> M
# B --> B
# C --> M
# D --> N
# E --> F
# F --> F

# Question 16
# A
os.getcwd()
os.chdir('C:/')
f = open('input_data.txt','r')
s = f.read()
print(s)
f.close()

======== RESTART: C:\Users\noaha\Downloads\Hartzfeld_Midterm2.py ========
Nauset:Eastham: 1837  3-10 Nauset.GIF 49
Three Sisters:Eastham: 1836 solid 3Sisters.GIF 15
Bass River:West Dennis :1853 1-6 BassRiver.GIF 44
Cape Cod:North Truro : 1797 1-5 Highland.GIF 66
Chatham:Chatham:1808 continuous chatham.GIF 43

# B
def make_LD():
    # sig nonetype --> dict{str:str}
    #returns dict mapping lighthouse to all other info
    f = open('input_data.txt','r')
    s = f.read()
    mydict = {}
    for line in s:
        split = line.split()
        mydict[split[0]] = split[1:]
    return mydict


# C

def is_lh(lighthouse,mydict):
    # sig str, dict{str:str} --> bool
    # returns True if the input is a lighthouse in the dictionary otherwise it returns False
    if lighthouse in mydict:
        return True
    else:
        Return False
    
           
# D

#SKIP



# E
class Lighthouse:

    def __init__(self,name,town,year,blink,img,height):
        # sig str,str,int,str,str,int --> nonetype
        # initiates the features of a ligthouse
        self.name = name
        self.town = town
        self.year = year
        self.blink = blink
        self.img = img
        self.height = height

# F
    def __str__(self):
        #sig nonetype --> str
        # prints this code if lighthouse object is created and printed
        return ('Name: ' + self.name + '/nTown: '+  self.name+'/nYear: '+ str(self.year)+'/nBlinking Pattern: '+ self.blink+'/n:Name of image file '+ self.img+'/nHeight: '+ str(self.height))
# Having an issue not letting me run should work sorry

  

# E
L1 = Lighthouse('Nauset','Eastham', 1837,'3-10','Nauset.GIF', 49)
L2 = Lighthouse('Three Sisters','Eastham',1836, 'solid', '3Sisters.GIF', 15)
# Having an issue not letting me run should work sorry
            
    
# G
# SKIP



