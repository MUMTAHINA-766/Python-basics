class Story_Book:

    no_of_books = 0

    def __init__(self, name, price, author,no_of_pages):


        self.name = name
        self.price = price
        self.author = author
        self.publish_yr = 2020
        self.no_of_pages = no_of_pages

        Story_Book.no_of_books += 1

    #regular method 1
    def get_book_info(self):
        print(f'The book name: {self.name},price:{self.price},pages:{self.no_of_pages}')
    #regular method 2
    def get_author_info(self):
        print(f'Autor name is: {self.author}')
    def apply_discount(self):
        self.price = self.price - self.price*self.discount

book1 = Story_Book('Teen Goyenda',300,'Rakibul Hasan',500)
book2 = Story_Book('Loraku',500,'Nasim Hijaji',1000)

# book1.get_book_info()
# book1.get_author_info()
# book2.get_book_info()
# book2.get_author_info()

# print(book1.no_of_books)
# print(book2.no_of_books)
print('Number of book',Story_Book.no_of_books)

print(f'{book1.name} book\'s actual price',book1.price)
book1.discount = 0.5
book1.apply_discount()
print(f'{book1.name} book\'s Discount price',book1.price)



