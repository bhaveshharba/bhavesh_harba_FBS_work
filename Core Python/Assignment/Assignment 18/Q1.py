# 1. Create a class Complex Number with data members as real and imag and add
# following methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator

class Complex_Number :
    def __init__(self, real = 0, imag = 0):
        self.real = real
        self.imag = imag

    def __del__(self):
        print('Destructor is called.')

    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return f'Addition is {real} + {imag}i'
    
    def __sub__(self, other):
        real = self.real - other.real
        imag = self.imag - other.imag
        return f'Substraction is {real} + {imag}i'
    

c1 = Complex_Number(3, 4)
c2 = Complex_Number(1, 2)

print(c1 + c2)
print(c1 - c2)