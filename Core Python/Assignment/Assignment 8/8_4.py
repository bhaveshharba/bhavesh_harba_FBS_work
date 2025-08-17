# 4. Sum of all odd numbers between 1 to n

def odd():

    num = int(input("enter a number: "))
    total_sum =0
    for i in range(1,num+1):
     if(i % 2 !=0):
       total_sum += i  
    print(f'sum of odd number between 1 to {num} is: ',total_sum)
odd()