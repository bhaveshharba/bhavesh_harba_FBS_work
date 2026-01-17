fp = open('File Handling/python_flow3.txt', 'w+')

print('Cursor pos ;', fp.tell())

fp.write('Core python')

print('Cursor pos :', fp.tell())

fp.seek(0,0)

print('Cursor pos :', fp.tell())

content = fp.read()
print(content)


fp.close()
