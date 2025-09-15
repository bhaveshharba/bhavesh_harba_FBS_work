# 6. Python Program to Find the Union of two Lists

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

union = []

for ele in list1:
    if(ele not in union):
        union.append(ele)

for ele in list2:
    if (ele not in union):
        union.append(ele)

print('Union of two lists is:',union)