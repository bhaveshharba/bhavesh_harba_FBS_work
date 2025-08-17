# 7. Write a program to print first n prime numbers.

n = int (input("enter a number: "))
count = 0
num = 2

while(count<n):
    for i in range(2,num//2+1):
        if(num % i ==0):
            break
    else:
     print(num,",", end= "")
     count+=1
    num+=1    
print(f'\nthese are first prime numbers')