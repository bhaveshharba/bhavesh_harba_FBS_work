class Rectangle:
    def setData(self,l,b):
        self.length = l
        self.breadth = b
    
    def showData(self):
        print('Length:',self.length)
        print('Breadth:',self.breadth)
    
    def areaOfRect(self):
        area = self.length * self.breadth
        return area
    
rect1 = Rectangle()
rect1.setData(40,20)
rect1.showData()
print('Area of Rectangle :',rect1.areaOfRect())


