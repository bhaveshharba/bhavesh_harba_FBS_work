# 12. Python Program to count number of lowercase characters in a string.

string = input('Enter String :')
lowercase = 0

for char in string:
    if(char.islower()):
        lowercase += 1

print('Count of lowercase character in string is',lowercase)