# 1. Create a class Book with members as bid,bname,price and author.Add following
# methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook
# d. Add static variable count and also maintain count of objects created.

class Book():
    count = 0
    def __init__(self,bid=1,bname='',price=0,author=''):
        Book.count += 1
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        
    def ShowBook(self):
        print(f'Book ID :{self.bid}\nBook name :{self.bname}\nPrice:{self.price}\nAuthor :{self.author}' )
        print('#################################################')

    def __del__(self):
        print('Destructor is called.')

    def total_count():
        print('Total books :',Book.count)

b1 = Book(101,'C',200,'XYZ')
b1.ShowBook()

b2 = Book(102,'Cpp',200,'ABC')
b2.ShowBook()

b3 = Book()
b3.ShowBook()

Book.total_count()


