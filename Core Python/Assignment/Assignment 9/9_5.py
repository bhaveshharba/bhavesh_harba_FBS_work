# 5. Write a program to find factorial using recursion.


def series(n):
    if n==0:
        return 1 
    else:
        return n * series(n-1)
    
num= int(input('Enter Number to check :'))
res = series(num)
print(res)