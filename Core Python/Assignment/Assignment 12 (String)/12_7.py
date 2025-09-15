# 7. Python Program to Calculate the Length of a String Without Using a
# Library Function

string = input('Enter String :')
count = 0

for char in string:
    count += 1

print('Length of string is',count)
