#Note :- it is a also type of polymorphism
#Ex- Addition of time

#Using 2 objects

class  Time:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s  = s

    def __add__(self,other):
        s = self.s + other.s
        m = s // 60
        s = s % 60
        m = self.m + other.m + m
        h = m // 60
        m = m % 60
        h = self.h + other.h + h
        return f'{h} : {m} : {s}'

t1 = Time(35, 43, 29)
t2 = Time(20, 34, 55)

print(t1 + t2)



#Using more than 2 objects

# class  Time:
#     def __init__(self, h, m, s):
#         self.h = h
#         self.m = m
#         self.s  = s

#     def __add__(self,other):
#         s = self.s + other.s
#         m = s // 60
#         self.s = s % 60
#         m = self.m + other.m + m
#         h = m // 60
#         self.m = m % 60
#         self.h = self.h + other.h + h
#         return self
        
#     def __str__(self):
#         return f'{self.h} : {self.m} : {self.s}'



# t1 = Time(35, 43, 29)
# t2 = Time(20, 34, 55)
# t3 = Time(20, 5, 4)

# print(t1 + t2 + t3)




