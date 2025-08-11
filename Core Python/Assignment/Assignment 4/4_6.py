# 6. WAP to check if a given number is prime number or not.

num = int(input('Enter Number To Check :'))
for i in range(2,num//2+1):                       
    if(num % i == 0):
        print(f'{num} is not a Prime Number')
        break
else:
    print(f'{num} is a Prime Number.')

