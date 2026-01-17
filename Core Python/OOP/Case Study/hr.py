from emp import Emp

class hr(Emp):
    def __init__(self, id, nm, basic,comm):
        super().__init__(id,nm,basic,'HR')
        self.comm = comm

    def calSal(self):
        da_amt = self.basic * 0.1
        hra_amt = self.basic * 0.12
        self.total_sal = self.basic + da_amt + hra_amt + self.comm

        # print(self.total_sal)

# h1 = hr(101,'ABC',10000,5000)
# h1.calSal()