# 1. Create a class Book with members as bid,bname,price and author.Add following
# methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook


class Book :
    def __init__(self,bid=1,bname=' ',price=0):
        self.id = bid
        self.name = bname
        self.price = price

    def ShowBook(self):
        print('Book ID :',self.id)
        print('Book Name :',self.name)
        print('Book Price :',self.price)

    def __del__(self):
        print('Destructor is called.')


b1=Book(101,'Python',500)           ##Parameterized constructor.
b1.ShowBook()

b2=Book()                           ## It is Parameterless Constructor but, basically
b2.ShowBook()                       ## it is default constructor.