# 2. Create a derived class from Student as EnggStudent with :
# a. Data members as :
    # i. Branch
    # ii. InternalMarks
# b. Add the following methods :
    # i. Parameterized constructor
    # ii. Display
    # iii. Accept
    # iv. override Method CalculateRank
    # v. Override __str__ Method

class Student():
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
    
    def display(self):
        print('Name :',self.name)
        print('Roll.No :',self.rollno)
    
# s1 = Student(101,'Ram')
# s1.display()

class EnggStudent(Student):
    def __init__(self, name='', rollno=0, branch='', internal_mark = 0, external_mark = 0):
        super().__init__(name, rollno,)
        self.branch = branch
        self.internal_mark = internal_mark
        self.external_mark = external_mark

    def Accept(self):
        self.name = input('Enter name of student :')
        self.rollno = int(input('Enter Roll.no :'))
        self.branch = input('Enter branch :')
        self.internal_mark = int(input('Enter internal mark :'))
        self.external_mark = int(input('Enter external mark :'))

    def display(self):
        super().display()
        
    def __str__(self):
        return f'Branch name :{self.branch}\nInternal Mark : {self.internal_mark}\nExternal Mark :{self.external_mark}'

    def CalculateRank(self):
        total = self.internal_mark + self.external_mark
        if (total >= 75):
            print ('Pass with Distinction')
        elif(total >= 65):
            print ('Pass with the First class')
        elif(total >= 50):
            print ('Pass with the Second class')
        elif(total >= 35):
            print ('Pass')       
        elif(total < 35):
            print ('Failed')
 

es1 = EnggStudent()
es1.Accept()
es1.display()
print(es1)
es1.CalculateRank()
