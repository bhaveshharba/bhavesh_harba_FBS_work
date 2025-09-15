# 6. Write a program to remove duplicates from the list.

li = [1, 2, 3, 2, 4, 1, 5, 3, 6]

new_li =[]

for ele in li:
    if(ele not in new_li):
        new_li.append(ele)

print('List after removing duplicates :',new_li)