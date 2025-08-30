# 7. Write a program to find sum of digits using recursion.

def sum_digit(n):
    if (n==0):
        return 0
    else:
        return (n%10) + sum_digit(n//10)
    
num = int (input('Enter Number :'))
res = sum_digit(num)
print(res)
