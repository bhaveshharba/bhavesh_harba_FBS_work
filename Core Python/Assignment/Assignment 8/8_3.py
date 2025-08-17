# 3. Write a program to find sum of following series using functions :
# a. 1+ 2 + 3 + 4+..... + n
# b. 1!+ 2! + 3! + 4!+..... + n!
# c. 1^1 + 2^2 + 3^3+ ...... n^n

def series_1 (n):
    sum = 0
    for i in range(1,n+ 1):
        sum += i
    print(f'Addition is {sum}')

num = int (input('Enter Number to check :'))

def series_2(n):
    for i in range(1,n+1):
        fact = 1
        sum = 0
        for j in range(1,i+1):
            fact *= j
            sum = sum + fact
    print(f'Addition of Factorial is {sum}')

def series_3(n):
    for i in range(1,n+1):
        sum = 0
        exp = 1
        for j in range(1,i+1):
            j **= j
            
        print(exp)
        exp += 1

# def series_3():
#     num = int(input("enter a number: "))
#     total =0
#     for i in range (1,num+1):
#         total += i**i
#     print(f'sum of series from 1 to {num} is ',total)
# exponensial()

# series_1(num)
# series_2(num)
series_3(num)