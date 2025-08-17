# 6. Write a program to find print the following Fibonacci series using
# functions:
# 1 1 2 3 5 8 n terms

def fibonacci ():
    num = int(input("enter a number: "))
    a = -1
    b = 1
    for i in range (0,num):
     c = a+b
     print(c)
     a = b
     b = c
fibonacci()