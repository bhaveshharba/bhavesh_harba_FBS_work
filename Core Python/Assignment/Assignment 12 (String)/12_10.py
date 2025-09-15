# 10.Python Program to Take in Two Strings and Display the Larger String
# without Using Built-in Functions

str1 = input('Enter First String :')
str2 = input('Enter Second String :')

count1 = 0
count2 = 0

for char in str1:
    count1 += 1

for char in str2:
    count2 += 1

if(count1>count2):
    print('Larger string is :', str1)
else:
    print('Larger string is :',str2)