from emp import Emp

class admin(Emp):
    def __init__(self, id, nm, basic,allowance):
        super().__init__(id,nm,basic,'Admin')
        self.allowance = allowance

    def calSal(self):
        da_amt = self.basic * 0.1
        hra_amt = self.basic * 0.12
        self.total_sal = self.basic + da_amt + hra_amt + self.allowance

        # print(self.total_sal)


# a1 = admin(101,'ABC',10000,5000)
# a1.calSal()