# 5. Sum of all prime numbers between 1 to n

def prime ():
    num = int(input("enter a number: "))
    total = 0
    for i in range(2,num+1):
        if(num%i==0):
         total +=i
        
    print(f'sum of prime num between 1 to {num} is',total)
prime()
