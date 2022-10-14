# Noah Hartzfeld
# Section 5
# 11/5/2020


# Question 1

'''
I am always accidentally typing variable names, or command name wrongs and thinking
my code is fine and not knowing why there is an issue

I simply have to type my code more carefully or choose shorter names that I am less likely
to misstype
'''



def classify_shape():
    # sig: None -> str
    # classifies shape based on number of sides and answers to questions
    # YorN = input ('Does the shape have a circular face or slice? (Y or N)')
    YorN='Y'
    if YorN == 'Y':
        YorN = input('Does the shape have an apex? (Y or N)')
        if YorN == 'Y':
            return 'cone'
        elif YorN =='N':
            YorN = input('Is the shape uniformly curved in all directions?')
            if YorN == 'Y':
                return 'oblate'
            else:
                YorN = input('Does the shape have two parallel circular faces?')
                if YorN == 'Y':
                    YorN = input('Are the circular faces connected by a surface at 90 degrees to both circles?')
                    if YorN == 'Y':
                        return 'right cylindrical prism'
                    else:
                        return 'irregular cylindrical prism'
                else:
                    return 'spheroid'

# Question 2
'''
There is an unexpected indent
'''

# Question 3
'''
It tells us the problem is below the if statement not above it 
'''

# Question 4
'''
There is still no error
'''

# Question 5
'''
We still have an indent error
'''

# Question 6
'''
Even with triple quotes there is an indent issue
'''

# Question 7

# Question 8
'''
There is a syntax error when returning the right cylindrical prism
'''

# Question 9
''' we should be returning a string right cylidrical prism instead we are returning a
variable so we need to put quotes around it
'''

# Question 10
'''
once I fixed the indentation issues below line 15, and the same syntax error in line 17
as 15 the code is debugged
'''

# Question 11

# Question 12


def sneaky_snake():
    # sig: none -> ??
    # What is this function doing?
    
    s='snake'
    x=0
    acc=''

    for i in s:
        if x%2==0:
            acc += i
        x+=3
    return acc

print(sneaky_snake())

# Question 13
'''
Var in loop     Loop1      Loop2     Loop3    Loop4     Loop5     return
i                 s          n         a        k         e        
x                 0          3         6        9         12       
acc              ''         's'       's'      'sa'      'sa'      'sae'
'''


# Question 14

def sneaky_snake2(x):
    acc = ''
    i = 0
    while i < len(x):
        acc += str(x[i])
        i += 2

    return acc
        
        











