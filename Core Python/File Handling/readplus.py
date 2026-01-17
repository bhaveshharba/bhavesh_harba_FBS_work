fp = open('File Handling/python_flow3.txt', 'r+')
print('Cursor position :', fp.tell())           #gives the cursor pos

content = fp.read()
print(content)

print('Cursor position :', fp.tell())

fp.write('\nthis is the next line.')

fp.seek(0,0)    #change cursor pos


content = fp.read()
print(content)


fp.close()






# for finding cursor pos use fp.tell

#for cursor pos change use fp.seek(0,0)
#in which first par is for char  and second par is 0 is for beginig, 1 is for current, 2 is for end.