# 11. Python Program to replace every blank space with hyphen in a string.

str = input('Enter String :')
res = '' 

for char in str:
    if(char in ' '):
        res += '-'
    else:
        res += char

print(res)