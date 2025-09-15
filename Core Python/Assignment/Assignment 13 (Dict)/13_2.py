# 2. Python Program to Concatenate Two Dictionaries Into One

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

result = {}

for key in dict1:
    result[key] = dict1[key]

for key in dict2:
    result[key] = dict2[key]

print(result)
