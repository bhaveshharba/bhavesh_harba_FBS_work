#1. method1

# import functions
# # print(functions.add(25,20)) 
# # print(functions.fact(4))
# # print(functions.checkEven(25))


#2. method2

# from functions import *
# print(add(30,40))


#3. method3

# from functions import add, checkEven
# print(add(45,10))
# print(checkEven(25))


#4. method4   - Alias name

from functions import checkEven as chEv     #----------Alias name
print(chEv(25))