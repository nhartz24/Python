# Noah Hartzfeld
# Section 5
# 10/05/2020


# Question 1

def remove_spaces(x):
    #sig str --> str
    #preconditions - must be a string
    #removes spaces from the word
    acc = ''

    for item in x:
        if item != ' ':
            
            acc += item

    return acc

# Question 2
def reverse(x):
    #sig str --> str
    #preconditions - must be a string
    #reverses the word
    acc = ''

    for item in x:
        acc = item + acc

    return acc


def is_palindrome(x):
    #sig str --> bool
    #preconditions - must be a string
    #finds if the entered word is a palindrome

    s = remove_spaces(x)
    r = reverse(s)
    

    if s == r:

        return True

    else:
        return False



#Question 3
def finder(needle,haystack):
    #sig str --> nonetype
    #preconditions - must be a string
    #checks to see if the shorter needle string is within the longer haystack string

    i = 0
    acc = []
    while i < (len(haystack) - (len(needle) - 1)):
        if (needle == haystack[i: (len(needle) + i)]):
            acc.append(i)
            i += 1
            
        else:
            i += 1

   
    if len(acc) > 0:
        print(acc[len(acc)-1])

    else:
        print('-1')

# Question 4
def title_case(s):
    #sig str --> str
    #preconditions - must be a string 
    #capitalizes the first letter in each word in a string
    acc = ''
    i = 1
    z = s[0]
    acc +=(z.upper())

    while i < len(s):

        if s[i] == ' ':
            acc += s[i]
            acc += s[(i + 1)].upper()
            i += 1 
        else:
            if s[i - 1] == ' ':
                i+=1
            else:
                acc += s[i]
                i += 1


    return acc








        
