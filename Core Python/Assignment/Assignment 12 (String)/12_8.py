# 8. Python Program to Remove the Characters of Odd Index Values in a
# String

str = input('Enter string :')
result = ''

i = 0
while(i<len(str)):
    if(i%2==0):
        result += str[i]
    i += 1

print(result)
