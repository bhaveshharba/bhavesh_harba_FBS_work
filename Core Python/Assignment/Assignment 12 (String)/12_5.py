# 5. Python Program to Count the Number of Vowels in a String

str = input('Enter string to check :')
count = 0

for char in str:
    if(char in 'aeiouAEIOU'):
        count += 1

print(count)
