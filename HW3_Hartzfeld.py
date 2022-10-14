# Noah Hartzfeld
# Section 05
# 09/20/2020

#Problem 1

'''
Predicted

A. print (thriceplusone(10)) will return 31

B. print (thriceplusone(thriceplusone(3))) will return 31

C. print (isdifferencesmall(thriceplusone(1),thriceplusone(2))) will return 9

D. print (isdifferencesmall(thriceplusone(5),thriceplusone(10))) will return none
'''

def thriceplusone (x):
    return (x * 3) + 1


def isdifferencesmall (a, b):
    diff = a - b
    sqr = diff * diff
    return sqr < 10


'''
A. print (thriceplusone(10))

========== RESTART: C:/Users/noaha/AppData/Local/Programs/Python/Python38-32/HW3_Hartzfeld.py =========
31

B. print (thriceplusone(thriceplusone(3)))

========== RESTART: C:/Users/noaha/AppData/Local/Programs/Python/Python38-32/HW3_Hartzfeld.py =========
31


C. print (isdifferencesmall(thriceplusone(1),thriceplusone(2)))

========== RESTART: C:/Users/noaha/AppData/Local/Programs/Python/Python38-32/HW3_Hartzfeld.py =========
True


D. print (isdifferencesmall(thriceplusone(5),thriceplusone(10)))

========== RESTART: C:/Users/noaha/AppData/Local/Programs/Python/Python38-32/HW3_Hartzfeld.py =========
False
'''


#Problem 2

def top (position):
    print (position * " " + "^")


def middle ( position , width ):
    print ( position * " " + "/" + width * " " + "\\")


def bottom ( position , width ):
    print ( position * " " + width * "-")
    

top(5)


middle(4,2)

middle(3,4)

middle(2,6)

middle(1,8)


bottom (0,12)

'''
========== RESTART: C:/Users/noaha/AppData/Local/Programs/Python/Python38-32/HW3_Hartzfeld.py =========
     ^
    /  \
   /    \
  /      \
 /        \
------------
'''



# Problem 3

pi = float(3.14)



def sqr(x):   # value entered must be float 
    return x*x 

def circlearea(r):            # r = radius of circle; value entered must be float
        return(sqr(r)*2*pi)

def cylindersurfacearea (r,h):  # h = height of cylinder; value entered must be float
        return (circlearea(r)*2*pi*r*h)


'''
A. print (sqr(2))

========== RESTART: C:/Users/noaha/AppData/Local/Programs/Python/Python38-32/HW3_Hartzfeld.py =========

4


B. print(circlearea(2))

========== RESTART: C:/Users/noaha/AppData/Local/Programs/Python/Python38-32/HW3_Hartzfeld.py =========

25.12


C. print (cylindersurfacearea(2,2))

========== RESTART: C:/Users/noaha/AppData/Local/Programs/Python/Python38-32/HW3_Hartzfeld.py =========

631.0144
'''
