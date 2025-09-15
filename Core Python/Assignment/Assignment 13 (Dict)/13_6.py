# 6. Python Program to Multiply All the Items in a Dictionary

dict = {'a': 1, 'b': 2, 'c': 3, 'd':4}
multiply = 1

for i in dict:
    multiply *= dict[i]

print(multiply)