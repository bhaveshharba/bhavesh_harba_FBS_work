# 9. Write a program to calculate the m to the power n using recursion.

def power(n,m):
    if m==0 :
        return 1
    else:
        return n * power(n,m-1)
    
n=int(input("enter number :"))
m=int(input("enter power :"))
result=power(n,m)

print(f'{n} power {m} is :',result)