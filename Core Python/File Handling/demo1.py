# fp = open('D:/FBS/core python/File Handling/python_flow.txt','r') #copy path
# fp = open('D:\FBS\Core Python\File Handling\python_flow.txt','r') #backward slash
fp = open('File Handling/python_flow.txt', 'r')

content = fp.read()
print(content)
fp.close()

# D:\FBS\Core Python\File Handling\python_flow.txt