# 2. Create a class Distance with data members as km,m and cm and add following
# methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator


class Distance:
    def __init__(self, km = 0, m = 0, cm = 0):
        self.km = km
        self.m = m
        self.cm = cm

    def __del__(self):
        print('Destructor is called')

    def __add__(self,other):
        cm = self.cm + other.cm
        m = cm // 100
        cm = cm % 100

        m = self.m + other.m + m
        km = m // 1000
        m = m % 1000
        km = self.km + other.km + km
        return f'Km :{km}, M :{m}, CM : {cm}'
  

d1 = Distance(1, 2000, 1000)
d2 = Distance(2, 1000, 500)

print(d1 + d2)
     