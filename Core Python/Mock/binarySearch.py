def binary_search(li,searchEle):
    low = 0
    high = len(li)-1

    while(low <= high):
        mid = (low + high) // 2

        if(li[mid] == searchEle):
            return mid
        elif(searchEle > li[mid]):
            low = mid + 1
        else:
            high = mid - 1
        
    return -1

li = [10,20,30,40,50]
num = int(input('Enter no :'))
res = binary_search(li,num)

if(res != -1):
    print(f'{num} found at index {res }')
else:
    print(f'{num} is not found.')