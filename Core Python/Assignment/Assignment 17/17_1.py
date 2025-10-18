# 1. Create a class Student with following
# a. data members :
    # i. StudentId
    # ii. Name
    # iii. Age
    # iv. Percentage
# b. Add the following methods :
    # i. Parameterized constructor
    # ii. Display
    # iii. Accept
    # iv. Method CalculateRank
    # v. Override __str__ Method

class Student():
    def DataMember(self,id=0,name='',age=0,percentage=0):
        self.id = id
        self.name = name
        self.age = age
        self.percentage = percentage

    def Accept(self):
        self.id = int(input('Enter id of student :'))
        self.name = input('Enter name of student :')
        self.age = int(input('Enter age of student :'))
        self.percentage = float(input('Enter percentage of student :'))

    def Display(self):
        print('ID :',self.id)
        print('Name :',self.name)

    def __str__(self):
        return f'Age :{self.age}\nPercentage :{self.percentage}'
    
    def CalculateRank(self):
        if (self.percentage >= 75):
            print ('Pass with Distinction')
        elif(self.percentage >= 65):
            print ('Pass with the First class')
        elif(self.percentage >= 50):
            print ('Pass with the Second class')
        elif(self.percentage >= 35):
            print ('Pass')       
        elif(self.percentage < 35):
            print ('Failed')

s1 = Student()
s1.Accept()
s1.Display()
print(s1)
s1.CalculateRank()
