# with the help of while loop we can run code infinite time



# 1. print helllo world 10 times

# i = 0
# while(i < 10):
#     print('Hello World!')
#     i = i + 1                # i += 1
# print('Program Succesfully completed.')




# 2. print 1 to 10

# i = 1
# while(i <= 10):
#     print(i)
#     i = i + 1                # i += 1




# 3 . print 1 to 10 reverse

# i=10
# while(i>=1):
#     print(i)
#     i = i-1





# 4. print 2s table

# i=1
# num = 2
# while(i<=10):
#     print(num * i)
#     i = i + 1




# 5. Write multiply table user want

# num = int(input('Enter Number :'))
# i=1
# while(i<=10):
#     print(num * i)
#     i += 1




# 6. Write a program to separte digit

# num = int(input('Enter Number :'))
# temp = num
# while(temp > 0 ):
#     d = temp % 10
#     print(d)
#     temp = temp // 10





# 7 to n print only even no. 

# n = int(input('Enter Number :'))
# i=1
# while( i <= n):
#     if(i % 2 == 0):
#         print(i)
#     i += 1




# 8 Addition of three digit number 


# num = int(input('Enter Three digit number :'))
# sum_of_digit = 0
# while(num > 0):
#     d = num % 10
#     sum_of_digit = sum_of_digit + d
#     num = num // 10  

# print(f'Sum of digit is {sum_of_digit}')



# 9 Find Factorial of num


# num = 5
# i = 1
# fact = 1 

# while(i<=num):
#     fact *= i
#     i += 1
# print(f'Factorial of {num} is {fact}.')


# Take number from user and calculate factorial of number


# num = int(input('Enter Number :'))
# i = 1
# fact = 1

# while(i<=num):
#     fact *= i
#     i += 1
# print(f'Factorial of {num} is {fact}.')



# 10 Number is strong or not
# 145 = 1! + 4! + 5!

   

num = int(input('Enter Number to check :'))
temp = num
sum = 0


while(temp>0):
    d = temp % 10
    temp = temp // 10 
    i=1
    fact = 1
    while(i<=d):
        fact *= i
        i += 1
    # print(fact)
    sum += fact

if(sum==num):
    print(f'{num} is Strong Number')
else:
    print(f'{num} is Not Strong Number')