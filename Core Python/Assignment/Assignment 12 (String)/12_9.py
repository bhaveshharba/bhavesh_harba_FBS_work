# 9. Python Program to Calculate the Number of Words and the Number of
# Characters Present in a String


string = input('Enter String :')

char_count = 0
word_count = 1

for char in string:
    char_count += 1

for char in string:
    if(char == ' '):
        word_count += 1

print(char_count)
print(word_count)