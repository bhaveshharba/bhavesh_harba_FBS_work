from emp import Emp

class Dev(Emp):
    def __init__(self, id, nm, basic,bonus):
        super().__init__(id,nm,basic,'S/W devloper')
        self.bonus = bonus

    def calSal(self):
        da_amt = self.basic * 0.1
        hra_amt = self.basic * 0.12
        self.total_sal = self.basic + da_amt + hra_amt + self.bonus

        # print(self.total_sal)

# d1 = Dev(101,'ABC',10000,5000)
# d1.calSal()