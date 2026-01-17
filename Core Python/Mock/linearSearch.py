def linear_search(li,searchEle):
    for ind in range(len(li)):
        if(li[ind] == searchEle):
            return ind
    else:
        return -1
        

li = [10,20,30,40,50]
num = int(input('Enter Number :'))

res = linear_search(li,num)

if(res != -1):
    print(f'{num} is found at index {res}.')
else:
    print(f'{num} is not found.')