# 5. Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

angle1 = int(input('Enter First Angle of Triangle :'))
angle2 = int(input('Enter Second Angle of Triangle :'))
angle3 = int(input('Enter Third Angle of Triangle :'))

if(angle1==angle2==angle3):
    print('Triangle is Equilaterall')
elif(angle1==angle2):
    print('Triangle is Isosceless')
elif(angle1 != angle2 != angle3):
    print('Triangle is Scalene')
else:
    print('Triangle is not Valid')