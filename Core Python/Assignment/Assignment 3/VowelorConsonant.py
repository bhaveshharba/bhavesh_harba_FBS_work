# 2. Write a program to input any alphabet and check whether it is vowel or consonant.

char = (input('Enter Character :'))
if(char in 'aeiouAEIOU'):
    print(f'{char} is Vowel.')
else:
    print(f'{char} is Consonant.')