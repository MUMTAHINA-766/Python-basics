class Story_Book:

    def __init__(self, name, price, author,no_of_pages):
        #setting the instance variables here

        self.name = name
        self.price = price
        self.author = author
        self.publish_yr = 2020
        self.no_of_pages = no_of_pages

#creating an instance /object of the Story_Book
    def get_book_info(self):
        print(f'The book name: {self.name},price:{self.price},pages:{self.no_of_pages}')
    def get_author_info(self):
        print(f'Autor name is: {self.author}')

book1 = Story_Book('Teen Goyenda',300,'Rakibul Hasan',500)
book2 = Story_Book('Loraku',500,'Nasim Hijaji',1000)

book1.get_book_info()
book1.get_author_info()
book2.get_book_info()
book2.get_author_info()

