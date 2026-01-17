#Inheritance 

#Single-levle inheritance



class Shape:
    def __init__(self,id,area):
        self.sid = id
        self.area = area

    def display(self):
        print('ID :',self.sid)
        print('Area :',self.area)

         
class Rectangle(Shape):
    def __init__(self, id, area,l,b):
         super().__init__(id, area)
         self.length = l
         self.breadth = b
    
    def display(self):
        super().display()
        print('Length :',self.length)
        print('Breadth :',self.breadth)


r1 = Rectangle('Rect1',800,80,20)
r1.display()
    
    
    