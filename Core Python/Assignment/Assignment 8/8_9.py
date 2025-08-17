# 9. Write a program to check if entered number is a palindrome or not.

def reverse_number(n):
    temp = n
    digit = 0
    while(temp > 0):
        digit = temp % 10
        temp = temp // 10
        print(digit)

num = int (input('Enter number :'))
reverse_number(num)

