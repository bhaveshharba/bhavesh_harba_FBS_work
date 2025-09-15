# 7. Python Program to Remove the Given Key from a Dictionary

dict = {'Name': 'C', 'ID':12, 'Author':'Ajay Mittal', 'Pub year':2014, 'Price':500}

key = input('Enter key to remove :')

result = {}

for i in dict:
    if(i != key):
        result[i] = dict[i]

print('Dictonary after removing',key,result)