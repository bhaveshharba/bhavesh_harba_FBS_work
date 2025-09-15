# #### Constructor
# 1.Constructor is magic method / special method which call automatically 
# when object is created.
# 2. __init__ name used as constructor name.
# 3. To bind values with attribute to self.

# #### Destructor
# 1. Destroctor is magic method / special methos which call automatically 
# when the scope of object is completed or object is deleted.
# 2. __del__ name used as destructor name.
# 3. It is used to released the resources, to close the database connection,
# or to close the network ports which used by object.
# Note : Destructor doesn't use to release attributes,states.


class Employee:
    def __init__(self,id,na,sal,dept):
        # print('This is constructor.')
        self.eid = id
        self.ename = na
        self.esal = sal
        self.edept = dept
        print('Constructor is called.')

    # def display(self):
    #     print('ID :',self.eid)  
    #     print('Name :',self.ename)
    #     print('Salary :',self.esal)
    #     print('Dept :',self.edept)

    def calSal(self):
        finalSal= 0
        hra = self.esal*10/100
        ta = self.esal*7/100
        pf = self.esal*12/100

        finalSal = self.esal - pf + hra + ta
        return finalSal

    def __del__ (self):
        print('Destructor is called.')

e1 = Employee(101,'Virat',18000,'CS')
# e1.display()
# print('Final Sal :',e1.calSal())
del e1

e2 = Employee(102,'Dhoni',70000,'WK')
# e2.display()
# print('Final Sal :',e2.calSal())