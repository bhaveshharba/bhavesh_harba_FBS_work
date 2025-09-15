# 2. Write a Python program to remove the intersection of a second set
# with a first set.

set1 = {1,2,3,4,5}
set2 = {1,2,6,7,8}

set1.difference_update(set2)
print('Set1 after removing intersection with Set2 :',set1)
