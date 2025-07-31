# 1. Write a program to find the area and perimeter of following figure (Accept the
# length, breadth and radius from user:

length = float(input('Enter length :'))
breadth = float(input('Enter Breadth :'))
radius = float(input('Enter Radius :'))

areaofrectangle=( length*breadth)
areaofsemicircle=(3.14*radius*radius)
area = (areaofrectangle+areaofsemicircle)

perimeterofrectangle =(2*length+breadth)
perimeterofcircle = (3.14*radius*radius)

perimeter = (perimeterofcircle+perimeterofrectangle)

print(f'Area is {area} and perimeter is {perimeter}')
