# 2. Write a program to check if given number is Armstrong or not using recursive
# # function.

def count(num,d,c):
    if(num==0):
        return 0
    else:
        d=num%10
        return (d**c) + count(num//10,c,d)

num=int(input("enter number = "))
c= len(str(num))
d=0
res1=count(num,d,c)
print(res1)

if(res1==num):
    print(f'{num} is Armstrong number.')
else:
    print(f'{num} is not Armstrong number.')

