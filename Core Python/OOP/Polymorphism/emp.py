# class Emp:
#     def __init__(self,id,name,sal,dept):
#         self.eid=id
#         self.ename=name
#         self.sal=sal
#         self.dept=dept
        
#     def __str__(self):
#         return f'{self.eid}, {self.ename}, {self.sal}, {self.dept}'
    
# e1=Emp(101,'ABC',4000,'SE')
# print(e1)


class vehicle:
    def start(self):
        print('Vehicle is started')

class car:
    def start(self):
        print('Car is started.')

v = vehicle()
c = car()

v.start()
c.start()