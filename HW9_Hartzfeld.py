# Noah Hartzfeld
# Section 5
# 11/15/2020

# Question 1

class Rectangle:
    def __init__(self, x, y, width, height):
        # sig int,int,int,int --> nonetype
        # initializes the variables for rectangle
        self.x = x
        self.y = y
        self.height = height
        self.width = width

# Question 2

    def compute_area(self):
        # sig nonetype --> float
        # returns the area of a created rectangle
        area = (abs(self.height * self.width))
        return area

# Question 4

    def translate(self):
        # sig nonetype --> list[int]
        # translates a rectangle to the origin adn returns it upper right point
        self.x = 0
        self.y = 0
        right = [abs(self.width), self.y]
        return right
'''
 width = (abs(self.width - self.x)
            length = (abs(self.length - self.y)
            right = [width,length]
            return right
            '''

r = Rectangle(0,0,2,3)
        


# Question 3

rect = Rectangle(1,0,7,2)
x = rect.compute_area()
'''
===================== RESTART: C:/Users/noaha/Downloads/HW8_Hartzfeld.py ====================
>>> x
14
'''

class Soup:

    def __init__(self, brand, volume, price):
        # sig str,float,float --> nonetype
        # initializes the variables for soup
        self.brand = brand
        self.volume = volume
        self.price = price

    def price_per_oz(self):
        # sig nonetype --> float
        # returns the price per ounce for a created soup, that is the most and\
        # least expensive, and is the best buy per ounce
        price = self.price/self.volume
        return price

candells = Soup('candells', 10.75, 1.75)
wespicks = Soup('wespicks', 10, 1.18)
valueright = Soup('valueright', 12, 1.8)
soups = [candells,wespicks,valueright]
def cans():
    # sig nonetype --> nonetype
    # prints the soup that holds the largest volume, 
    acc = 0
    acc2 = 0
    acc3 = 10
    acc4 = 10
    acc5 = []
    for soup in soups:
        if soup.volume > acc:
            acc = soup.volume

    for soup in soups:
        if soup.price > acc2:
            acc2 = soup.price

    for soup in soups:
        if soup.price < acc3:
            acc3 = soup.price

    for soup in soups:
        value = soup.price_per_oz()
        if value < acc4:
            acc4 = value

    for soup in soups:
        if soup.volume == acc:
            acc5.append(soup.brand)

    for soup in soups:
        if soup.price == acc2:
            acc5.append(soup.brand)

    for soup in soups:
        if soup.price == acc3:
            acc5.append(soup.brand)

    for soup in soups:
        if soup.price_per_oz() == acc4:
            acc5.append(soup.brand)

    print(acc5[0],'sells the largest portions,', acc5[1], 'is the most expensive,',\
          acc5[2], 'is the least expensive, and', acc5[3], 'is the best buy per ounce.')
          



        



    
