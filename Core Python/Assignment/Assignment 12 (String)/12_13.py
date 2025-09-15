# 13. Python Program to count number of digits and letters in a string.

string = input('Enter String :')
digit_count = 0
letter_count = 0

for char in string:
    if(char.isalpha()):
        letter_count += 1
    elif(char.isdigit()):
        digit_count += 1

print('Total digits in string is :',digit_count)
print('Total letters in string is :',letter_count)