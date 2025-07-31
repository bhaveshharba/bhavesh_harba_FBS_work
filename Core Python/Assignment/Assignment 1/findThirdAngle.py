# 6 Write a program to input two angles from user and find third angle of the triangle.

angle1 = int(input("enter the first angle"))
angle2 = int(input("enter the secound angle"))

third_angle = 180 - (angle1 + angle2)

print(f"the third angle of the triangle is {third_angle}.")