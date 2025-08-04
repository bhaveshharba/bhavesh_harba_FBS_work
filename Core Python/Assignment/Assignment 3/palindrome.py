# 12. Write a program to check if given 3 digit number is a palindrome or not.

num = int(input('Enter three digit number :'))
temp=num

d1 = temp%10
temp = temp//10

d2 = temp%10
temp = temp//10

d3 = temp%10
temp = temp//10

rev_num= ((d3*100)+(d2*10)+d1)

if(num==rev_num):
    print(f'{num} is Palindrome Number.')
else:
    print(f'{num} is Not Palindrome Number.')
