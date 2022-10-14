# Lab 4 Loops 
# 2020-02-17 KMT

# I. Bolean Expressions Review
# Question 1 Boolean Expressions
"""
x=3 y=5

Symbols        Words         
x==y           the value of x is equal to the value of y   False
x+2!=y         two more than x is not equal to y           False
x+(-6)>y       x plus negative six is greater than y       False
x<y+2          x is less than two more than y              True
"""
"""
>>> x=3
>>> y=5
>>> x==y
False
>>> x+2!=y
False
>>> x+(-6)>y
False
>>> x<2+y
True
>>> """

# II. Logical Operators
# Question 2
x=1
"""
x<5 and x>10
True and False -> False"""

"""
x<7 or x>12
True or False -> True"""
"""
not (x > 0)
not True -> False"""
"""
x and 3<5
True and True -> True"""
"""
>>> x<5 and x>10
False
>>> x<7 or x>12
True
>>> not (x > 0)
False
>>> x and 3<5 
True
Note any nonzero number evaluates to True
"""

# III. Conditional Statements

# Question 3
print('\nQuestion 3')
def check_x(x):
    """
    sig int or float -> None
    evaluates x and prints a statement"""
    if x > 0:
        print('x is positive')
    elif x ==0:
        print('x equals 0')
    else:
        print('x must be negative')

#A.
check_x(1)
#B.
check_x(-1)

# Question 4
print('\nQuestion 4')
def check_x_nest(x):
    """
    sig int or float -> None
    evaluates x and prints a statement"""
    if x == 0:
        print('x equals 0')
    else:
        if x >0:
            print('x is positive')
        else:
            print('x must be negative')

check_x_nest(-1)
check_x_nest(0)
check_x_nest(1)

# Part IV. Modulus Revisited
# Question 5
print('\nQuestion 5')
def modulus(x):
    """
    sig: int or float -> Bool
    returns Bool telling if x is odd or even"""
    if x%2 ==0:
        return True
    else:
        return False

modulus(1)
modulus(-16)

# Question 6
"""
The modulus will be 0"""
# Question 7
print('\nQuestion 7')
def mod_X_Y(X,Y):
    '''
    sig: int,int-> Bool
    returns True if X is evenly divisible by Y, otherwise False'''
    if X%Y==0:
        return True
    else:
        return False
print(mod_X_Y(56,5))
print(mod_X_Y(56,8))



# V. While Statements
# Question 8
print('\nQuestion 8')
def count_by_two(x):
    """
    sig: int -> none
    pre: x<10
    prints count up to 10 by twos"""
    while x <=10:
        print(x)
        x+=2 # augmented assignment
    print('You win!')

count_by_two(0)

# Question 9
print('\nQuestion 9')

# validation loop
while True:
    x=0#int(input('Please input an integer less than 10'))
    if x< 10:
        print('Thank you for your valid input.')
        break
    else:
        print('Sorry that is not valid input. Please try again.')
        
"""
The validation loop begins with a variable assignment in which x is
assigned to the value returned by the int function operating on the
result of the input function.  The user is prompted to enter an integer
less than 10. However, recall that input always represents the input as
a string.  Thus we apply an implicit conversion to integer.

If the integer is less than 10 and thereby meeting the desired criterion,
a positive message is sent to the user, and the while loop breaks, sending
execution outside the loop.  However, if the integer is not less than 10,
an error message is sent, the loop guard still evaluates to True, and the
user is again prompted to input an integer via the input function.

Note that this loop does not handle the case where the user enters input
that can not be converted to int format, such as 'two'.  Be on the lookout
for ways to deal with this and other potential errors in upcoming lectures!
"""


# Question 10
#count_by_two(x) #sends validated input


# Exercise: Rock Paper Scissors

"""
COMP112
Lab 4

Rock, Paper, Scissors

starter file

See the lab description for instructions on how to complete the program below.
"""

import random

def get_computer_move():
    """
    signature: () -> str
    returns one of 'rock', 'paper' or 'scissors' each time it is called.
    """
    return random.choice (['rock' , 'paper' , 'scissors'])


def is_valid(move):
    """
    signature: str -> bool
    returns True just in case the move is one of 'rock', 'paper', or 'scissors'
    """
    if move == 'rock' or move == 'paper' or move == 'scissors':
        return True
    else:
        return False


def get_player_move():
    """
    signature: () -> str
    returns the player's move, which must be one of 'rock', 'paper' or 'scissors'.
    """
    while True:
        move=input('Please enter your move: rock, paper, or scissors')
        if is_valid(move):
            return move
        else:
            print('Sorry that is not a valid input. Please try again.')


def play_game():
    """
    signature: () -> NoneType
    interactively conducts a game of rock-paper-scissors between the player and the computer.
    """
    player_score = 0
    computer_score = 0
    
    while player_score < 3 and computer_score < 3 :
        print('Comp:',computer_score,'\nPlayer:',player_score)
        player_move=get_player_move()
        computer_move=get_computer_move()
        print('Computer:',computer_move, '\nPlayer:',player_move)
        
        if player_move == computer_move:
            print('Tie round!')
        # rock vs paper: paper wins
        elif player_move=='rock' and computer_move=='paper':
            computer_score +=1
            print('Computer wins this round!')
        elif computer_move=='rock' and player_move=='paper':
            player_move +=1
            print('Player wins this round!')
            
        # paper vs scissors: scissors wins
        elif player_move=='paper' and computer_move=='scissors':
            computer_score+=1
            print('Computer wins this round!')
        elif computer_move=='paper' and player_move=='scissors':
            player_score+=1
            print('Player wins this round!')
            

        # scissors vs rock: rock wins
        elif player_move=='scissors' and computer_move=='rock':
            computer_score+=1
            print('Computer wins this round!')
        elif computer_move=='scissors' and player_move=='rock':
            player_score+=1
            print('Player wins this round!')
        else:
            print('Something went wrong.')
        
    
    print \
    ('The ' + ('human' if player_score > computer_score else 'computer') + ' is the winner!')


play_game ()  #  uncomment once you have implemented the play_game function above.








