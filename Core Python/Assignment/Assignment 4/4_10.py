# 10. WAP to check if given number is Perfect Number.

num=int(input("enter number= "))
t=0
for i in range(1,num):
    if(num%i==0):
        t=t+i

if(num == t):
    print(f'{num} is perfect number')
else:
    print(f'{num} is not perfect number')
