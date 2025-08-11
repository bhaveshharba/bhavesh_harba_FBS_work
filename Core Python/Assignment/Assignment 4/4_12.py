# 12. WAP to print Armstrong number within a given range

num=int(input("enter number= "))

for n in range(num+1):
    sum=0
    temp= n
    while(temp>0):
        digit=temp%10
        sum= sum + digit**3
        temp=temp // 10

    if n==sum:
        print(n)