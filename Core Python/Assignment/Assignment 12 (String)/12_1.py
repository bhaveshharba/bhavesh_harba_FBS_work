# 1. Python Program to Replace all Occurrences of ‘a’ with $ in a String

str = 'This is a demo string'
newstr = ''

for char in str:
    if(char in 'aA'):
        newstr += '$'
    else:
        newstr += char

print(newstr)
