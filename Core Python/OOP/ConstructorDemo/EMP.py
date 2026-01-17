# #### Constructor
# 1.Constructor is magic method / special method which call automatically 
# when object is created.
# 2. __init__ name used as constructor name.
# 3. To bind values with attribute to self.

#Types:
#1.Default, 2.Parameterized

class Employee:
    def __init__(self,id,na,sal,dept):
        print('This is constructor.')
        self.eid = id
        self.ename = na
        self.esal = sal
        self.edept = dept

    def display(self):
        print('ID :',self.eid)  
        print('Name :',self.ename)
        print('Salary :',self.esal)
        print('Dept :',self.edept)


e1 = Employee(101,'Virat',18000,'CS')
e1.display()

e2 = Employee(102,'Dhoni',70000,'WK')
e2.display()


 