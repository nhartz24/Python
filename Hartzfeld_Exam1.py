# Noah Hartzfeld
# Section 5
# 10/08/2020


# Section A

'''
1. F
2. T
#3. T
4. F
5. F
'''

# Section B

'''
6. N - variable name cannot begin with a number
7. Y
8. N - @ is not allowed in a variable name
9. Y
'''

# Section C

'''
#10. D
#11. A
12. C
13. A
'''


# Part 2


#14.
def print_i(i):
    #sig int -> int
    #precondition i must be a number between 1 nad 10
    #counts by twos up to ten from a given number between 1 and 10
    while i >= 1 and i <= 10:
        print (i)
        i += 2


#15.

def enter_letter():
    #sig nonetype -> nonetype
    i = False
    while i == False:
        x = input('Please enter a capital letter')
        f = is_cap_alpha(x)

        if f == True:
            print('Thank you for entering a capital letter :' , x)
            i = True
        else:
            print('This is not a valid input')
            i = False
        

def is_cap_alpha(x):
    # str -> bool
    if x.isupper():
        return True
    else:
        return False



# 16.
def shopping_cart_total_bug():
    # sig: NoneType -> float
    # pre: assume prices are in whole dollars only; 
    # decimals are not entered
    # returns the total of the prices of the items in the cart
    
    total = 0 #an accumulator named total to print out the to print out the total price of the items
    price = '' # definind price
    while price != 'Done': # price not defined
        price = input('Please input the price. Type Done to exit.')
        if price == 'Done':
            print('Thank you. Item entry is complete.\nYour total is')
            print('Your total is $' , float(total))
            return float(total)           #break should return the total of the prices not just break
        elif price.isdigit():      
            total+= int(price) #strings and ints cannot be combined
        else:
            print('That is not a valid price. Try again.')
    #return we should return after done is entered


'''
17. Implicit coersion is when pythin automatically converts a value to a specific type.
    input('Please enter a number')
    when the user enters 5 you would think it would be type int, but it is actually implicitly
    coerced by python to type string
'''

'''
18. Overloading is when an operator can perform tasks on multiple types
    The * opperator can multiply ints together such as 5*5 = 25, but it can also concatinate strings
    such as 5*'H' = HHHHH this is two completly different opperations in python hense the overload
'''


# Part 3

# 19.

# A.

def extract_year(YMD):
    i = 0
    j = ''
    while i < len(YMD):
        if YMD[i] == '-':
            j = YMD[0 : i]
            return j
        else:
            i+=1

def mystery(YMD):
    # sig: str -> int
    # pre: we assume the YMD string contains at least one dash
    # returns the slice position of first dash
    i = 0
    while i < len(YMD):
        if YMD[i] == '-':
            return i
        else:
            i+=1

def nmonth_2_NameMonth(x):


    if x == 1:
        return 'January'

    elif x == 2:
        return 'February'

    elif x == 3:
        return 'March'

    elif x == 4:
        return 'April'

    elif x == 5:
        return 'May'

    elif x == 6:
        return 'June'

    elif x == 7:
        return 'July'

    elif x == 8:
        return 'August'

    elif x == 9:
        return 'September'

    elif x == 10:
        return 'October'

    elif x == 11:
        return 'Novermber'

    elif x == 12:
        return 'December'

    else:
        return 'NoMonth'



# G.
'''
print('Final test') = Final test
print(convert_date('2020-10-08')) = October 8, 2020.
print(convert_date('2020-7-7')) = July 7, 2020.
print(convert_date('2020-10-10')) = October 10, 2020.
print(convert_date('2020-15-15')) = NoMonth 15, 2020.
'''











    
