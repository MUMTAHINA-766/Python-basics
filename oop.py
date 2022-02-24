"""
#create class create object
class BookInfo:
    pass #an empty block
p = BookInfo()
print(p)

"""
#object method
"""
class StoryBook:
    pass

book1 = StoryBook()
book2 = StoryBook()

book1.name = 'Kishor_golpo'
book1.price = 300
book1.author = 'Kazi Ismail Hossain'

book2.name = 'GRE quant'
book2.price = 350
book2.author = 'Dr. Sarwatullah'

print(book1.name,'\n',book2.name)
"""
"""

class Person:
    def sayHi(self):
        print('Hello, How are you?')
p = Person()
p.sayHi()
"""

"""
class Person:


    def __init__(self, name):
        self.name = name
    def sayHi(self):
        print('Hello,my name is ', self.name)

p = Person('Mumtahina')
p.sayHi()
#Person('Mumtahina').sayHi()

"""


class Story_Book:

    def __init__(self, name, price, author):
        #setting the instance variables here

        self.name = name
        self.price = price
        self.author = author
        self.publish_yr = 2020

#creating an instance /object of the Story_Book

book1 = Story_Book('Teen Goyenda',300,'Rakibul Hasan')
book2 = Story_Book('Loraku',500,'Nasim Hijaji')

print(book1.name,book1.publish_yr)
print(book2.name, book2.publish_yr) 


    

