# 2. Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# d. Constructor (Support both parameterized and parameterless)
# e. Destructor
# f. ShowProduct

class Product:
    def __init__(self,pid=0,pname=' ',price=0,quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quan = quantity

    def ShowProduct(self):
        print('Product ID :',self.pid)
        print('Product Name :',self.pname)
        print('Price :',self.price)
        print('Quantity :',self.quan)

    def __del__(self):
        print('Destructor is called.')

p1 = Product(101,'Hot Wheels',500,2)
p1.ShowProduct()

p2 = Product()
p2.ShowProduct()


