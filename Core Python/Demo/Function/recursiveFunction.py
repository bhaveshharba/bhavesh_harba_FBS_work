# Q.WAP to print sum of 1 to n numbers

def sos(n):
    if (n==0):
        return 0
    else:
        return n + sos(n-1)

n = int (input('Enter Number'))
sum = sos(n)
print(sum)



# Q. WAP to calculate factorial of number.

# def factorial(n):
#     if (n==0):
#         return 1
#     else:
#         return n*factorial(n-1)

# n = int(input('Enter Number to check :'))
# fact = factorial(n)
# print(fact)



# Q. WAP to print fibonacies series

# def fibo(n,a,b):
#     if(n>0):
#         c = a + b
#         print(c)
#         fibo(n-1,b,c)

# num = int(input('Enter Number :'))
# a=-1
# b=1
# fibo(num,a,b)


# # Q. WAP program to print sum of digit.

# def sod(n):
#     if(n == 0):
#         return 0
#     else:
#         return (n % 10) + sod(n // 10)

# num = int(input('Enter number :'))
# print (sod(num))
