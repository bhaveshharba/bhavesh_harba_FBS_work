# 4. Create a class College which has collection of students. Add the
# following methods :
# a. Parameteried constructor for number of students.
# b. AddStudent
# c. GetStudent
# d. RemoveStudent
# e. Override _str_ Method

class College :
    def __init__(self,num_student):
        self.students = [None]*num_student

    def addStudent(self,student_name):
        for i in range(len(self.students)):
            if self.students[i] is None:
                self.students[i] = student_name
                return f"Student '{student_name}' added"
        return 'No space to add more student'
    
    def getStudent(self,student_name):
        if student_name in self.students :
            index = self.students.index(student_name)
            return self.students[index]
        else:
            return f"Student '{student_name}' not found."
        
    def remove_student(self,student_name):
        if student_name in self.students :
            self.students.remove(student_name)
            return f"Student '{student_name}' removed."
        return f"Student '{student_name}' not found."

num_stud = int(input('Enter number of student you want to add college :'))
MIT = College(num_stud)

choice = 0
while(choice != 4):
    print('''Select choice :
          1. Add Student
          2. Get Student
          3. Remove Student
          4. Exit''')
    
    choice = int(input('Enter choice :'))

    if(choice == 1):
        std_name = input('Enter student name you want to add :')
        print(MIT.addStudent(std_name))
    elif(choice == 2):
        std_name = input('Enter student name you want to get detail :')
        print(MIT.getStudent(std_name))
    elif(choice == 3):
        std_name = input('Enter student name you want to remove :')
        print(MIT.remove_student(std_name))
    elif(choice == 4):
        print('Thank you!!!')
    else:
        print('Invalid choice.')