# 3. Write a program to input angles of a triangle and check whether triangle is valid or not.

angle1 = int(input('Enter First Angle of Triangle :'))
angle2 = int(input('Enter Second Angle of Triangle :'))
angle3 = int(input('Enter Third Angle of Triangle :'))

if(angle1+angle2+angle3==180):
    print('Triangle is Valid')
else:
    print('Triangle is Not Valid')