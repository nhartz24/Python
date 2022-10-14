# Noah Hartzfeld
# Section 5
# 10/04/2020

'''
# Question 1


def indices(x,xs):
    # sig (ints, strings, floats) --> int
    # preconditions x must be smaller in length than xs
    # searches for any words within a list that matches a given word and returns their indices
    acc = []
    i = 0
    for index in xs:
        if x == index:
             acc.append(i)
             i += 1
        else:
            i += 1

    return acc



# Question 2

def avg(x):
    # sig floats --> floats
    # precinditions msut be float values
    # avergaes the numbers in a given list
    acc = 0
    i = 0
    for value in x:
        acc += value
        i += 1

    return (acc / i)


# Question 3

def some_sum(x):
    # sig ints --> ints
    # preconditions must be ints
    # adds up all positive numbers in a list until a zero is reached
    acc = 0

    for value in x:
        if value > 0:
            acc += value
        elif value == 0:
            break

    return acc


# Question 4

def dedup(x):
    # sig ints, floats, strs --> ints, floats, strs
    # finds any repeats within a lsit and removes them
    acc = []
    for value in x:
        if value in acc:
            pass

        else:
            acc.append(value)


    return acc


def dedup_mut(x):
    # sig ints, floats, strs --> ints, floats, strs
    # finds any repeats within a lsit and removes them

    acc = []
    z = 0
    while z < len(x):
        if x[z] in acc:
            x.pop(z)

        else:
            acc.append(x[z])
            z += 1

    
    return x
'''

# 1

def indices(x,xs):
    i = 0
    acc = []
    while i < len(xs):
        if x == xs[i]:
            acc.append(i)
        i += 1
    return acc
    '''
    i = 0
    acc = []
    for char in xs:
        if x == char:
            acc.append(i)
        i += 1

    return acc
    '''

# 2

def average(x):
    i = 0
    acc = 0
    while i < len(x):
        acc += x[i]
        i += 1
    return acc / i

    '''
    acc = 0
    i = 0
    for char in x:
        acc += char
        i += 1
    mean = acc/i
    return mean
'''
# 3

def sum_some(x):
    acc = 0
    i = 0
    while i < len(x):
        if x[i] > 0:
            acc += x[i]
            i += 1
        elif x[i] < 0:
            i += 1
        else:
            break
    return acc

    '''
    acc = 0
    for char in x:
        if char > 0:
            acc += char
        elif char < 0:
            pass
        else:
            break
    return acc
'''

# 4

def dedup(x):
    acc = []
    i = 0
    while i < len(x):
        if x[i] not in acc:
            acc.append(x[i])
        i += 1
    return acc

    '''
    acc = []
    for char in x:
        if char not in acc:
            acc.append(char)
    return acc
'''


def dedup_mut(x):
    acc = []
    i = 0
    while i < len(x):
        if x[i] not in acc:
            acc.append(x[i])
            i += 1
        elif x[i] in acc:
            x.pop(i)
    return x
        

    
            
            
        

        
