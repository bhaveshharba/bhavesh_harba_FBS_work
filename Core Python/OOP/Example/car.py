class Car:
    def setData(self,brand,color,price):
        self.brand = brand
        self.color = color
        self.price = price
    
    def ShowData(self):
        data = f'BRAND:{self.brand}\nCOLOR:{self.color}\nPRICE:{self.price}'
        return data
    
    def start(self):
        print('Car started.')

    def stop(self):
        print('Car stopped.')

c1 = Car()
c1.setData('Toyota','Black',500000)
print(c1.ShowData())
c1.start()
c1.stop()
 