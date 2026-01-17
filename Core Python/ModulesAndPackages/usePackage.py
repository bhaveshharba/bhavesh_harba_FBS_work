# # # method1.
# from myPackage import myfunction

# print(myfunction.add(10,20))


# method2.
# from myPackage.myfunction import *

# print(add(10,20))


# # method3.
# from myPackage.myfunction import division

# print(division(10, 2))


# method4
from myPackage.myfunction import division as div

print(div(10, 2))  