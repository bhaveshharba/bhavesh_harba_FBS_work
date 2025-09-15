# Count total word fron string without using inbuilt function

str = 'Firstbit solution'
count = 1
for char in str:
    if (char == ' '):
        count += 1
print('Total words :',count)