# 8. Write a program to check whether a number is prime or not using recursion.

def prime(num):
    if(num==0):
        return 0
    else:
        for i in range(2,num//2+1):
            if(num%i==0):
                return False
        else:
            return True

num=int(input("enter number = "))
result=prime(num)

if(result):
    print("entered number is prime ")
else:
    print("entered number is not pime number ")