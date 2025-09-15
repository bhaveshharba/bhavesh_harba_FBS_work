# 1. Print Even Number 

# n = int(input('Enter Number to Check :'))
# for num in range (1, n+1):
#     if(num % 2 == 0):
#         print(num,end ='')



# 2. Print Prime Number or Not

num = int(input('Enter Number To Check :'))
for i in range(2,num//2+1):
    if(num % i == 0):
        print(f'{num} is not a Prime Number')
        break
else:
    print(f'{num} is a Prime Number.')





# 4. WAP to print Fibonacci series upto n

# num = int(input("Enter number of terms: "))
# a = -1
# b = 1

# for i in range(num):
#     c = a + b
#     print(c)
#     a = b
#     b = c


# temp = num
# total = 0
# for i in range(1,4):
#     d = temp % 10
#     total + total * 10 + d

