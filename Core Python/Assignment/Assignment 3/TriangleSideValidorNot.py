# 4. Write a program to input all sides of a triangle and check whether triangle is valid or not.

side1= int(input('Enter First Side of Triangle :'))
side2= int(input('Enter Second Side of Triangle :'))
side3= int(input('Enter Third Side of Triangle :'))

if((side1+side2>side3)):
    print('Triangle is valid')
else:
    print('Triangle is Not valid')