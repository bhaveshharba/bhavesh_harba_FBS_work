class Emp:
    def __init__(self,id,name,sal):
        self.id= id         #Public
        self._name= name    #Protected
        self.__sal= sal     #Private

e1=Emp(101,'Aman',6000)
print(e1.id)
# print(e1.__sal)
print(e1._name)


print(e1._Emp__sal)
        