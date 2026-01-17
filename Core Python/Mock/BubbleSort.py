

def bubbleSort_li(li):
    for i in range(1,len(li)):
        for j in range(0, len(li)-i):
            if(li[j]> li[j+1]):
                li[j],li[j+1] = li[j+1],li[j]
    return li


li = [60,50,40,30,20,10]
print('List before sort',li)

li = bubbleSort_li(li)
print('list after sort :', li)

