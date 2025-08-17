# 7. Write a program to find sum of digits of a number.


def sum():
    num = int(input("enter a number: "))
    
    temp = num
    
    d1 = temp % 10
    temp = temp //10
    d2 = temp % 10
    temp = temp // 10
    d3 = temp % 10
    temp = temp // 10
    
    sum = d1+d2+d3
    print(f'sum of digit is:',sum)
sum()

