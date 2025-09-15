# 3. Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# g. Constructor (Support both parameterized and parameterless)
# h. Destructor
# i. ShowShirt

class Shirts :
    def __init__(self,sid=0,sname=' ',type=' ',price=0,size=' '):
        self.id = sid
        self.name = sname
        self.type = type
        self.price = price
        self.size = size

    def ShowShirt(self):
        print('Shirt ID :',self.id)
        print('Shirt Name :',self.name)
        print('Shirt Type :',self.type)
        print('Price :',self.price)
        print('Size :',self.size)

    def __del__(self):
        print('Destructor is called')




s1 = Shirts(101,'Double Pocket','Casual',800,'Large')
s1.ShowShirt()

s2 = Shirts()
s2.ShowShirt()