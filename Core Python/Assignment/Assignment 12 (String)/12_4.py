# 4. Python Program to Form a New String where the First Character and
# the Last Character have been Exchanged

string = input('Enter string :')
res = ''

if(len(string)<=2):
    res = string
else:
    last_char = string[-1]
    first_char = string[0]
    middle_char = string[1:-1]
    
    res = last_char + middle_char + first_char

print('String after exchange',res)
