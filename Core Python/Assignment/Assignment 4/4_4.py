# 4. WAP to print factorial of a number .

num = int(input('Enter number to check :'))
i = 1
fact = 1
while(i<=num):
    fact = fact *i
    i += 1
print(f'Factorial of {num} is {fact}.')