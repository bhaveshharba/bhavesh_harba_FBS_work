# 15. Python Program to find larger string without using built-in functions.

str1 = input('Enter first string :')
str2 = input('Enter second string :')

count1 = 0
count2 = 0

for char in str1:
    count1 += 1

for char in str2:
    count2 += 1

if(count1 > count2):
    print('Larger string is :',str1)
else:
    print('Larger string is :',str2)