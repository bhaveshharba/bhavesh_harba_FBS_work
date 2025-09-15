# 5. Accept a number from user and check if this element is present in the list or
# # not. Also tell how many times it is present in the list.

def search(li,searchEle):
    for ind in range(len(li)):
        if(li[ind]==searchEle):
            return ind
    else:
        return -1
        
li=[12,35,7,84,53]
searchEle = int (input('Enter number to search :'))
res = search(li,searchEle)

if(res != -1):
    print(f'{searchEle} is found at index {res}.')
else:
    print(f'{searchEle} is not found in the list.')