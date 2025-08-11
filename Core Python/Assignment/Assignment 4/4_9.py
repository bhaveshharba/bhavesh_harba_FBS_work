# 9. WAP to print all numbers in a range divisible by a given number.

num=int(input("Enter number :"))
num1=int(input("Enter divisible number :"))

for i in range(1,num+1):
    if(i%num1==0):
        print(i,end=' ')