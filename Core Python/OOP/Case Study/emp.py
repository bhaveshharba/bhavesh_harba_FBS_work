from abc import ABC,abstractmethod

class Emp(ABC):
    def __init__(self,id,nm,basic,dept):
        self.eid = id
        self.name = nm
        self.basic = basic
        self.dept = dept
        self.total_sal = 0

    @abstractmethod
    def calSal():
        pass

