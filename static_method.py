class Story_Book:

    no_of_books = 0

    def __init__(self, name, price, author,no_of_pages):


        self.name = name
        self.price = price
        self.author = author
        self.publish_yr = 2020
        self.no_of_pages = no_of_pages
        Story_Book.no_of_books += 1

    # #regular method 1
    # def get_book_info(self):
    #     print(f'The book name: {self.name},price:{self.price},pages:{self.no_of_pages}')
    # #regular method 2
    # def get_author_info(self):
    #     print(f'Autor name is: {self.author}')
    # def apply_discount(self):
    #     self.price = self.price - self.price*self.discount
    # #method to change price
    # def set_price(self, new_price):
    #     self.price = new_price
    ##CLASS method 1
    # @classmethod
    # def set_discount(cls, new_discount):
    #     cls.discount = new_discount

    ##class method 2
    @classmethod
    def construct_from_string(cls, book_str):
        name, price, author, no_of_pages = book_str.split(',')
        return cls(name,price,author,no_of_pages)

    ##static method
    def is_new(publish_yr):
        if publish_yr> 2021:
            print("Yes, It is a new book.")
        else:
            print('It is not new.')




book1 = Story_Book('Teen Goyenda',300,'Rakibul Hasan',500)
book2 = Story_Book('Loraku',500,'Nasim Hijaji',1000)



# print('Number of book',Story_Book.no_of_books)

# print(f'{book1.name} book\'s actual price',book1.price)
# book1.discount = 0.5
# book1.apply_discount()
# print(f'{book1.name} book\'s Discount price',book1.price)

# print(book1.price)
# print(book1.discount)

# Story_Book.set_discount(0.6)
# book1.apply_discount()
# print(book1.price)

#method2
book_str = 'Mathematics,500, Dr. Hafizul Bari, 1200'
mathbook = Story_Book.construct_from_string(book_str)
print(mathbook.name, mathbook.price, mathbook.author, mathbook.no_of_pages)
#static
Story_Book.is_new(book1.publish_yr)