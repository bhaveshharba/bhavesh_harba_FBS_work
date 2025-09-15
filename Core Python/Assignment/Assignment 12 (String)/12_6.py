# 6. Python Program to Take in a String and Replace Every Blank Space
# with Hyphen

string = input('Enter a string :')
result = ''

for char in string:
    if(char in ' '):
        result += '-'
    else:
        result += char
print(result)