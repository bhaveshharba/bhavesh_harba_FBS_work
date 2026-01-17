from emp import Emp
class softDev(Emp):
    def __init__(self, name, age, id, sal,tech):
        super().__init__(name, age, id, sal)
        self.tech = tech

    def display(self):
        return super().display()+f'\nTECH :{self.tech}'
    

sd = softDev('XYZ',27,102,35000,'Python')
print(sd.display())