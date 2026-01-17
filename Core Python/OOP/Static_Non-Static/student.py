#Static Variable.

class Student :
    count = 0
    def __init__(self,roll_no,name,age):
        Student.count += 1
        self.roll_no = roll_no
        self.name = name
        self.age = age
    
    def display_Data(self):
        pass

    def totalStudent():
        print('Total Student :',Student.count)


s1 = Student(11,'Abc',13)

s2 = Student(12,'xyc',14)

Student.totalStudent()