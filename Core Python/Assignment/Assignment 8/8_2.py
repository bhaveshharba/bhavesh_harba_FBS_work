# 2. Write a program to calculate area of circle

def area_of_circle (r):
    area = 3.14 * r * r
    print(f'Area of Circle is {area}')

radius = float(input('Enter radius of circle :'))

area_of_circle(radius)