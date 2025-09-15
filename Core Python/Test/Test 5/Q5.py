# 5. Python program to find the union of two lists without using set concept.
li1 = []
li2 = []
len1 = int(input('Enter length of first list :'))
for i in range(len1):
    num1 = int(input('Enter number for first list :'))
    li1.append(num1)


len2 = int(input('\nEnter length of second list :'))
for i in range(len2):
    num2 = int(input('Enter number for second list :'))
    li2.append(num2)

union = []

for ele in li1:
    if (ele not in union):
        union.append(ele)

for ele in li2:
    if(ele not in union):
        union.append(ele)


print('List 1 :',li1)
print('List 2 :',li2)
print('Union of list is :',union)




