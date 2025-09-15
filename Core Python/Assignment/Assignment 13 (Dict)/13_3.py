# 3. Python Program to Check if a Given Key Exists in a Dictionary or Not

dict = {'Name': 'C', 'Author':'Ajay Mittal','Pub year':2014}
search = input('Enter key to search :')

key_exist = False

for key in dict:
    if(key==search):
        key_exist= True
        break

if(key_exist):
    print(f'key:{search} exist in dictionary.')
else:
    print(f'key:{search} not exist in dictionary.')