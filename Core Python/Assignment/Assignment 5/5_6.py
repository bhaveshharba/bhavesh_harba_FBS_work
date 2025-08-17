# 6. Write a program to print prime numbers between 1 to 100.

n=25
count = 0
num = 2
print("prime number between 1 to 100 : ",end=' ')
while(count<n):
    for i in range(2,num//2+1):
        if(num % i ==0):
            break
    else:
     print(num,",",end= "")
     count+=1
    num+=1    
