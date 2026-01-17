
class Pollymorphism:
    def add(n1,n2):
        return n1+n2

    def add(n1,n2,n3):
        return n1+n2+n3


p1 = Pollymorphism

print('Addition is',p1.add(10,20,30)) #O/P
print(p1.add(10,20))    #Error
    
# print(p1.add(10,20))      #Error
# print(p1.add(10,20,30))   #Error
    
