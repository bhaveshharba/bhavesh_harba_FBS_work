class  Fan:
    def setData(self,brand,color,price):
        # print('It is setData method.')
        self.b = brand
        self.c = color
        self.p = price
    
    def display(self):
        # print('It is display method')
        print('Brand:',self.b)
        print('Color:',self.c)
        print('Price:',self.p)

    def toStart(self):
        print('Fan is start.')

    def toStop(self):
        print('Fan is stop.')

    def toIncrease(self):
        print('Increasing speed sucessful')

    def toDecrease(self):
        print('Decreasing speed sucessful')

    


obj1 = Fan()
obj1.setData('Godrej','White','2500')
obj1.display()
obj1.toStart()
obj1.toStop()
obj1.toIncrease()
obj1.toDecrease()

print('###############################')

obj2 = Fan()
obj2.setData('Bajaj','Black',6000)
obj2.display()




