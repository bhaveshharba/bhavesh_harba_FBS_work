# 3. Create a class MedicalStudent inherited from Student with following
# a.
    # i. Data members :Specialization
    # ii. MarksOfInternship
# b. Add the following methods :
    # i. Parameterized constructor
    # ii. Display
    # iii. Accept
    # iv. override Method CalculateRank
    # v. Override __str__ Method



class Student():
    def __init__(self,name='', rollno=0):
        self.name = name
        self.rollno = rollno

    def Display(self):
        print('Name :',self.name)
        print('Roll.No :',self.rollno)

    def CalculateRank():
        pass

# s1 = Student(101,'Ram')
# s1.Display()

class MedicalStudent(Student):
    def __init__(self, name='', rollno=0, specialization='', MarksofInternship = 0):
        super().__init__(name, rollno)
        self.specialization = specialization
        self.MarkofInternship = MarksofInternship

    def Accept(self):
        self.name = input('Enter Name :')
        self.rollno = int(input('Enter Rollno :'))
        self.specialization = input('Enter Specialization :')
        self.MarkofInternship = int(input('Enter Marks of Internship :'))

    def Display(self):
        super().Display()

    def __str__(self):
        return f'Specialization :{self.specialization}\nMarks of Internship :{self.MarkofInternship}' 


    def CalculateRank(self):
        if (self.MarkofInternship >= 90):
            print('Distinction')
        elif(self.MarkofInternship >= 80):
            print ('First Rank')
        elif(self.MarkofInternship >= 70):
            print ('Second Rank')
        elif(self.MarkofInternship >= 60):
            print ('Average')
        elif(self.MarkofInternship >= 50):
            print ('Pass')       
        elif(self.MarkofInternship <= 49):
            print ('Failed')
        
ms1 = MedicalStudent()
ms1.Accept()
ms1.Display()
print(ms1)
ms1.CalculateRank()


    


  
