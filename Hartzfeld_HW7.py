# Noah Hartzfeld
# Section 5
# 10/25/2020

'''
# Question 1

respellings = {"teh": "the", "relevent": "relevant", "lite": "light", "lol": "haha"}

def respell(x):
    # sig str --> str
    # references the dict respellings to fix commonly mispelled words and return the phrase with proper spelling
    s = x.split()
    i = 0
    z = 0
    acc = ''
    for char in s:
        if char in respellings:
            s[i] = respellings[char]
            i += 1

        else:
            i += 1

    for char in s:
        if z < (len(s) - 1):
            acc += (char + ' ')
            z += 1
        else:
            acc += char
            z += 1

    return acc


# Question 2

def wordpositions(x):
    # sig str --> dict(str,int)
    # counts the numebr of times a word is in a string
    s = x.split()
    myD = dict()
    i = 0
    for char in s:
        if char not in myD:
            myD[char] = [i]
            i += 1

        else:
            myD[char] += [i]
            i += 1

    return myD


# Question 3

def most_common(x):
    # sig str --> str
    # returns the most common word in a string
    s = wordpositions(x)
    vals = s.values()
    acc = []
    for char in vals:
        if len(char) > len(acc):
            acc = char

        else:
            pass
    
    for char in s:
        if s[char] == acc:
            return char

# Question 4

# A
def resolve_phone_number(forwards,num):
    # sig dict(int), int --> int
    # returns the final forwarded phone for the given office phone
    acc = num
    for char in forwards:
        if char == acc:
            acc = forwards[char]
            
    return acc

# B
def resolve_phone_number2(forwards,num):
    # sig dict(int) --> int or str
    # returns the forwarded phone, or returns circular if it the phone is forwarded back to itself
    acc = num
    for char in forwards:
        if char == acc:
            acc = forwards[char]
            
        if forwards[char] == num:
            return "circular"
            
    return acc
'''

respellings = {'teh': 'the', 'relevent': 'relevant', 'lite': 'light', 'lol': 'haha'}

def respell(x):
    acc = []
    s = x.split()
    acc3 = []
    for word in s:
        if word in respellings:
            acc.append(word)
            
    for word in s:
        if word in respellings:
            acc3.append(respellings[word])
        else:
            acc3.append(word)

    h = ' '
    y = h.join(acc3)
    return y
    
'''
        if word in respellings:
            acc2 += (' ' + respellings[word])
        elif s[0] == word:
            acc2 += word
        else:
            acc2 += ' ' + word
    return acc2
'''



def wordpositions(x):
    split = x.split()
    mydict = {}
    i = 0
    for word in split:
        if word not in mydict:
            mydict[word] = [i]
        else:
            mydict[word] += [i]
            
        i += 1
    return mydict


def common(x):
    mydict = wordpositions(x)
    acc = ''
    for char in mydict:
        if len(mydict[char]) > len(acc):
            acc = mydict[char]

    for char in mydict:
        if mydict[char] == acc:
            return char


# 4

def dialing(forwards, num):
    for char in forwards:
        if forwards[num] == char:
            forwards[num] = forwards [char]
    return forwards[num]



def circle(forwards,num):
    for char in forwards:
        if forwards[num] == char:
            forwards[num] = forwards [char]
        elif forwards[num] == num:
            return 'circular'

    return forwards[num]

    







    




