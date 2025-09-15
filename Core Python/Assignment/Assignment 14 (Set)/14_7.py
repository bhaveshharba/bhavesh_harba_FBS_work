# 7. Given two sets of numbers, write a Python program to find the missing
# numbers in the second set as compared to the first and vice versa.
# Use the Python set.

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

print('Numbers missing in second set compared to first set :',set1.difference(set2))
print('Numbers missing in first set compared to second set :',set2.difference(set1))