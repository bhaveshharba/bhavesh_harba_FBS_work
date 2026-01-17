#syntax for importing :- from file_name import class_name


from person import Person
class Emp(Person):
    def __init__(self, name, age,id,sal):
        super().__init__(name, age)
        self.eid=id
        self.salary =sal

    def display(self):
        return super().display()+f'ID :{self.eid}\nSalary :{self.salary}'
    
# e1 = Emp('ABC',30,101,35000)
# print(e1.display())