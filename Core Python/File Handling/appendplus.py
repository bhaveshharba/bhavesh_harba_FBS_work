fp = open('File Handling/python_flow3.txt', 'a+')

print('Cursor pos :', fp.tell())

fp.write('\nFirstbit solution')

print('Cursor pos :', fp.tell())

fp.seek(0,0)
content = fp.read()
print(content) 








