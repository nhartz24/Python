# Noah Hartzfeld
# Section 5
# 10/22/2020

# Part 1

cap2state = dict()
'''
>>> type(cap2state)
<class 'dict'>
'''

cap2state['Hartford'] = 'Connecticut'
'''
>>> cap2state
{'Hartford': 'Connecticut'}
'''

cap2state = {'Monpelier':'Vermont', 'Augusta':'Maine', 'Concord':'New Hampshire', 'Providence':'Rhode Island'}
'''
>>> cap2state
{'Monpelier': 'Vermont', 'Augusta': 'Maine', 'Concord': 'New Hampshire', 'Providence': 'Rhode Island'}
'''

cap2state['Boston'] = 'Massachusetts'
cap2state['Hartford'] = 'Connecticut'
'''
>>> cap2state
{'Monpelier': 'Vermont', 'Augusta': 'Maine', 'Concord': 'New Hampshire', 'Providence': 'Rhode Island', 'Boston': 'Massachusetts', 'Hartford': 'Connecticut'}
'''

cap2state['Hartford'] = 'Wyoming'
'''
>>> cap2state
{'Monpelier': 'Vermont', 'Augusta': 'Maine', 'Concord': 'New Hampshire', 'Providence': 'Rhode Island', 'Boston': 'Massachusetts', 'Hartford': 'Wyoming'}
'''

# Question 1

cap2state['Hartford'] = 'Connecticut'
'''
{'Monpelier': 'Vermont', 'Augusta': 'Maine', 'Concord': 'New Hampshire', 'Providence': 'Rhode Island', 'Boston': 'Massachusetts', 'Hartford': 'Connecticut'}
'''

# Question 2 
cap2state['Middletown'] = 'Connecticut'
'''
>>> cap2state
{'Monpelier': 'Vermont', 'Augusta': 'Maine', 'Concord': 'New Hampshire', 'Providence': 'Rhode Island', 'Boston': 'Massachusetts', 'Hartford': 'Connecticut', 'Middletown': 'Connecticut'}
'''
# Keys are not mutable

# Question 3

'''
>>> 'Rhode Island' in cap2state
False
'''
# the in operator only searches for keys not values

vals = cap2state.values()
'''
>>> vals
dict_values(['Vermont', 'Maine', 'New Hampshire', 'Rhode Island', 'Massachusetts', 'Connecticut', 'Connecticut'])
'''

# Question 4
'''
>>> 'New Hampshire' in vals
True
'''


# Part 2

# Question 5
def histogram(mystring):
    # sig --> dict(str:int)
    # makes a dictionary histogram of letters
    myD = dict()
    for char in mystring:
        if char not in myD:
            myD[char] = 1
            
        else:
            myD[char] += 1
            
    return myD

        
# Question 6
def miscount():
    # sig none --> int
    # counts the total letters in Mississippi
    hist = histogram('Mississippi')
    vals2 = hist.values()
    acc = 0
    for char in vals2:
        acc += char

    return acc


# Question 7
hist = histogram('Mississippi')
'''
>>> hist.keys()
dict_keys(['M', 'i', 's', 'p'])
'''
