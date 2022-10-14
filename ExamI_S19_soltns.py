# Program Exam I Spring 2019
# Prof. Kelly M. Thayer
# COMP 112 S19
# Exam I. Introduction to Programming
# 2019-02-27
#


#######_PART_I_TRUE_AND_FALSE_MULTIPLE_CHOICE###########################################################

# Question 1.
'''
1.	T    F   Accumulator is an example of a Python type.
'''
# False.

# Question 2.
'''
2.	T    F   Functions lacking a return statement do not return anything.
'''
# False.

# Question 3.
'''
3.	T    F   ‘Xylophone’ < ‘bassoon’
>>> 'Xylophone'<'bassoon'
True '''
# True

# Question 4.
'''
4.	T    F   int(5.999999)//3==2
>>> int(5.999999)//3==2
False
>>> int(5.999999)//3
1
>>> '''
#False

# Question 5.
'''
5.	T    F   given x=’True’ type(x)returns <class 'str'>.
>>> x='True'
>>> type(x)
<class 'str'>
>>> 
'''
# True

#Question 6.
'''
6.	            x = ‘violincello’    # goes to question 6
T    F   x[10:0]==x[-11:11]
>>> x = 'violincello'
>>> x[10:0]==x[-11:11]
False
>>> x[10:0] #the indices are right to left which always gives empty string
''
>>> x[-11:11]
'violincello'
>>> '''
# False

# Question 7.
'''Andante! # illegal because of punctuation
>>> Andante!=1
SyntaxError: invalid syntax'''
# False

# Question 8.
'''2ndFiddle # illegal because it begins with a digit.
>>> 2ndFiddle=1
SyntaxError: invalid syntax'''
# False

# Question 9.
'''AlTo_SaXoPhOnE # valid
>>> AlTo_SaXoPhOnE=1
>>>'''
# True

###Multiple Choice

# Question 10
'''
Augmented Assignment.  Which  of the following is an example of valid augmented assignment? (Assume all variables are defined but the type of x is purposely not specified.)

i.	x = x + 1 # valid syntax but not augmented assignment
ii.	x+=12     # yes
iii.	x += acc  # yes

A.	i
B.	ii
C.	iii
D.	both ii and iii 
'''
# D

# Question 11
'''
11.  Variable type.  Read the snippet from an interactive python session on the Idle interpreter.  Select the answer that best describes the type of the variable x. This shows the Python interpreter.

>>> x  = int(input(‘Please enter an integer.’))
Please enter an integer. 3 
3
>>> type(x)

A.	x is an integer. The user typed the integer 3, which was implicitly coerced to a string by input, and int explicitly coerced it back to an integer.
B.	x is an integer because the user typed 3 which is type int instead of ‘3’ which would be a string or 3.0 which would be a float.
C.	x is an integer; It has been implicitly coerced into an integer.
D.	x is a string; input always takes a string for input.
'''
# A

# Question 12
'''
12. Variable assignment.  Shown is a Python variable assignment. Select the letter of the best equivalency.
x = x * 2    

A.	x gets the value of two times x
B.	The current value of x in the variable table is overwritten by 2 times the current value of x.
C.	Both sides could be divided out by x, which would give 1=2 which is a false statement, so Python will return False.
D.	Both A and B accurately describe the variable assignment.
'''
# D

#####_PART_II_SHORT_ANSWER

'''
14. Linear Conditional.  What will the output be when this code is run?
Circle the letter(s) of all that apply. 

A.	x is less than 0
B.	x is less than or equal to 0
C.	x equals 0
D.	x is greater than or equal to 0
E.	x is greater than 0
F.	‘None’
G.	(none of the above apply) '''
print('Question 14. Linear Conditional')

def linear_conditional(x):
    # signature: int -> none
    # preconditions: x is an integer
    # evaluates if-block
    
    if x < 0:
        print('x is less than 0')
    elif x <= 0:
        print('x is less than or equal to 0')
    elif x == 0:
        print ('x equals 0')
    elif x >= 0:
        print ('x is greater than or equal to 0')
    elif x > 0:
        print ('x is greater than 0')

linear_conditional(0)
'''
>>> ================================ RESTART ================================
>>> 

Question 14. Linear Conditional
x is less than or equal to 0
'''
# B


# Question 15
'''
15.  Nested Conditional.  What will the output be when this code is run?
Circle the letter(s) of all that apply.
A.	x is less than or equal to 0
B.	x equals 0, instance 1
C.	x is greater than or equal to 0
D.	x equals 0, instance 2
E.	‘None’
F.	(none of the above apply)
'''
def nested_conditional(x):
    # signature: int -> nonetype
    # preconditions: x is an integer
    # evaluates if-block

    if x <= 0:
        print('x is less than or equal to 0')
        if x == 0:
            print('x equals 0, instance 1')
    elif x >= 0:
        print ('x is greater than or equal to 0')
        if x == 0:
            print('x equals 0, instance 2')

print('Question 10. Nested Conditionals')
nested_conditional(0)
'''
Question 10. Nested Conditionals
x is less than or equal to 0
x equals 0, instance 1 '''

# A and B


# Question 16. X or O
'''
16.  X or O.  Consider the XorO function:'''
def XorO(n):
    # signature: int -> str
    # preconditions: n is an integer
    # pass
    T = n%2
    if T == 0:
        return 'X'
    else:
        return 'O'
'''

A.  Part of the heading is missing.  Write a description for the function to
replace pass.

returns X if the input is even and O if the input is odd.

B. How many parameters does the function have?

The function has one parameter, namely n.

C.  What are the local variables?

Local variables: n, T

'''

# Question 17. Spot the bug Shopping Cart
'''
17.  Spot the Bug Shopping cart.
The following program should keep track of the running total of
the merchandise in the cart and return the total. Write what the
problem(s) is/are and correct the code by editing it.'''

def shopping_cart2():
    # signature: (none) -> float
    # preconditions: none
    # computes the total of items in the cart.You may presume the user
    # inputs numeric values; you do not have to check the input for being
    # numeric.

    total=0
    while True:
        
        x=float(input('Please input the price of the item in US Dollars.0 to exit'))
        if x==0:
            print('Goodbye!')
            return total
        elif x < 0:
            print('We are not paying you to shop here!')
        else:
            total += x
            
def shopping_cart(): # THIS HAS BUGS!
    # signature: (none) -> float
    # preconditions: the user types valid prices
    # iteratively computes the total of items in the cart and returns the total.

    
    while True:
        total=''# empty quotes # (1)move outside loop  (2) 0 instead of ''
        # (3) you need float bc the input will be a string
        x=(input('Please input the price of the item in US Dollars.0 to exit'))
        if x==0:
            print('Goodbye!')
            # (4)  # return total is needed here and not below
        elif x < 0:
            print('We are not paying you to shop here!')
        else:
            total += x    
        return total # (4) this will break the function the first time through the loop
#                    note that moving it outside the loop creates an infinite loop
#                    because there is no break or return in a while True.

#print(shopping_cart2())


# Question 18. Overloading
'''
18.  Overloading.  Name an operator that we have encountered in the class that
exhibits overloading.  Then provide two examples of the operator use that
illustrate the overloading.

One of these:
+ does integer addition and concatenates

* does multiplication and replication of strings

'''
print('Question 18. Overloading')
print('Addition: 2 + 2 =',2+2)
print('Concatenation: "2"+"2":','2'+'2')
print('Multiplication: 3 * 2=',3*2)
print('Replication: "3" *2=',"3"*2)

# Question 19. Double W

def double_W(s):
    s = s.upper()
    i=0
    acc='X'
    for x in s:
        if x == 'W':
            acc = 2*acc 
        elif x == 'U':
            acc = s[i] + acc + s[i]
    return acc


print('Question 19. Double W')
"""
A.	What will Python print for the shown function call?
print(double_W('WU'))"""
print(double_W('WU'))
# WXXW

'''
B.	Write a function call showing the input that will return the string ‘TXTTXT’.
'''
print(double_W('TUW'))

'''
Question 19. Double W
WXXW
TXTTXT'''

#print(double_W('TUVWXYZ'))
#print(double_W('UUU'))
#print(double_W('WWW'))


#####_PART_III._CODE_WRITING_################

'''
Question 20. Famous Last Words
A. The function get_alpha_space_only takes a string and strips out all characters other than the 26 English alphabet letters and also preserves spaces.  Punctuation, digits, etc. should be stripped out.  Complete the function to do the task.

def get_alpha_space_only(s):
    # signature: str -> str
    # preconditions: you may presume that s is guaranteed to be type string
    # returns only alphabetic and space characters in original order.

	pass

'''

def get_alpha_space_only(s):
    # signature: str -> str
    # preconditions: you may presume that s is guaranteed to be type string
    # returns only alphabetic and space characters in original order.

    acc=''
    for x in s:
        if x.isalpha():
            acc += x
        elif x == ' ':
            acc += x
    return acc
'''
B. Removing end spaces 
def remove_endspaces(s):
    # signature: str -> str
    # preconditions: presume s is guaranteed to be type string
    # removes end spaces
    acc='' #empty quotes
    acc2='' #empty quotes
    # reverse the input
    for x in s:
        acc = x + acc
    i=0
    seen_alpha=False
    while i < len(acc):
        if acc[i]==' ' and seen_alpha==False:#space in quotes
            i+=1
        else:
            acc2 = acc[i] + acc2
            seen_alpha=True
            i+=1
    return acc2

Above is shown the completed function remove_endspaces.  Explain how the function achieves removing the end spaces.  In your explanation, include the following points:
a.	An overview of the code and how it works
The code removes the end spaces. It achieves this by reversing the input
and looking to see if it has encountered any alphabetic characters yet.
In the even that it does, then removing spaces will not be necessary
and it re-reverses the string and returns it. In the case there are
spaces, it does not transfer the spaces to the new accumulator. Upon
getting to the alphabetic characters, it will then start adding them.


b.	Why seen_alpha is needed
It is needed to keep track of whether an alphabetic character has been seen.
The copying to the accumulator will begin when the alphabetic characters
are found.  It has the effect of adding spaces inside the sentence but not
at the beginning (which in the reversal is the end.)

c.	Why the input is reversed
This is done so that the search can use a for look to check for the space at
the beginning. Pulling from the end will not work well with the mechanism
in place.


'''

def remove_endspaces(s):
    # signature: str -> str
    # preconditions: presume s is guaranteed to be type string
    # removes end spaces
    acc='' #empty string
    acc2=''
    # reverse the input
    for x in s:
        acc = x + acc
    i=0
    seen_alpha=False
    while i < len(acc):
        if acc[i]==' ' and seen_alpha==False:
            i+=1
        else:
            acc2 = acc[i] + acc2
            seen_alpha=True
            i+=1
    return acc2

'''
C.	 Convert the for loop within remove_endspaces into a while loop

'''

def remove_endspaces_2Whiles(s):
    # signature: str -> str
    # preconditions: presume s is guaranteed to be type string
    # removes end spaces
    acc=''
    acc2=''
    # reverse the input
    # using a while loop instead of the if 
    i = 0                 # this is the answer!
    while i < len(s):     #
        acc = s[i] + acc  #
        i+=1              #

    i=0
    seen_alpha=False
    while i < len(acc):
        if acc[i]==' ' and seen_alpha==False:
            i+=1
        else:
            acc2 = acc[i] + acc2
            seen_alpha=True
            i+=1
    return acc2

print('2 Whiles')
print(remove_endspaces_2Whiles('This is the last word I have to write   ')+'END')

"""
D.	 The famous_last_words function is started for you.  Complete the function by replacing pass with code. The function should return the last alphabetic word from a string input s. As a clue, consider that the words are separated by a space character and assume that there are not any spaces at the end of the string.

def famous_last_words(s):
    # signature: str -> str
    # preconditions: presume that s is type string and the last character is not a space
    # returns the last alphabetic word from the input string s

    acc=''
    for x in s:
        pass
    return acc
"""


def famous_last_words(s):
    # signature: str -> str
    # preconditions: presume that s is type string and the last character is not a space
    # returns the last alphabetic word from the input string s

    acc=''
    for x in s:
        if x ==' ': # quotes contain space
            acc = '' # reset to a new word empty quotes
        elif x.isalpha():
            acc +=x
    return acc
'''
E.	 Here is an input string. Note it has 2 spaces at the end of the string. 

myinput=('These!.are.the?.last words I have to say.!  ')

Write the function calls to execute the three functions above to get the last word out of the myinput string. You may use composition and/or any  necessary variables.  Your code should do the following:
-get the alphabetic and space characters from the myinput string
-remove any extra  spaces at the end of the input
-extract the last word say from the input string
'''


myinput=('These!.are.the?.last words I have to say.!  ')

#'A string that has a space at the end'
x1=(get_alpha_space_only(myinput))  
print(x1)
x2=remove_endspaces(x1)
print(x2)
x3=famous_last_words(x2)
print(x3)




# Question 21.
"""
21.  Diamond in the snow box.  20 points.  Write a function that prints the diamond in the box shown below for the case n=5 and n=7.  Your code should take an input parameter n that indicates the width of the diamond at the middle.  All other lines should be written relative to the n parameter.  For reference, a solution to the pyramid homework problem is provided. Like the pyramid problem, assume n is a positive odd integer. (You do not need to write code to screen the input.)

def pyramid(n):
    x=1
    while x <= n:
        print((n//2-x//2)*' ' + x*'-')
        x+=2

# diamond in the snow box n=5

*******
***-***
**---**
*-----*
**---**
***-***
*******

# diamond in the snow box n=5

*********
****-****
***---***
**-----**
*-------*
**-----**
***---***
****-****
*********

"""


def diamond_in_snow(n):
    x=1
    print((n+2)*'*')
    while x <= n:
        print(((n//2-x//2)+1)*'*' + x*'-'+((n//2-x//2)+1)*'*')
        x+=2
    x-=4
    while x > 0:
        print(((n//2-x//2)+1)*'*' + x*'-'+((n//2-x//2)+1)*'*')
        x-=2
    print((n+2)*'*')
    
diamond_in_snow(5)
print()
diamond_in_snow(7)


def pyramid(n):
    x=1
    while x <= n:
        print((n//2-x//2)*' ' + x*'-')
        x+=2

print('pyramid base 5:')
pyramid(5)
"""
print('pyramid base 15:')
pyramid(15)
print('pyramid base 25:')
pyramid(25)
"""

    
# program for a little while

def for_loop(s):
    A='' #empty string
    B='' #empty string
    for x in s:
        if x.isupper():
            A += x
        elif x.isdigit():
            B += x
    return B + ' ' + A #quotes contain space

print(for_loop('mOV1EuRs8iT1UcR2E'))
# A.
'''
A.	 What will python print?'''
#1812 OVERTURE

#B.
'''
B.	Briefly describe how the code works. (A few sentences is sufficient.)
The function extracts characters from the input if they are either upper
case by using the .isupper() method or extracting digits using the .isdigit()
method.  Each are sent to their respective accumulators.  Finally the
extracted words are presented in the return statement.'''



# C.
"""
C.	Convert the for loop to a while loop that will give the same output.
"""
def while_loop(s):
    A='' #empty string
    B='' #empty string
    i=0
    while i < len(s):
        if s[i].isupper():
            A += s[i]
        elif s[i].isdigit():
            B += s[i]
        i+=1
    return B + ' ' + A #quotes contain space

print(while_loop('mOV1EuRs8iT1UcR2E'))










