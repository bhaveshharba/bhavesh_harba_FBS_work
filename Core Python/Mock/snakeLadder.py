num = 100

for i in range(1,11):
    if (i % 2 != 0):
        for j in range(num,num-10,-1):
            print(j,end=' ')
        num -= 10
    else:
        for j in range(num-9,num+1):
            print(j,end=' ')
        num -= 10
    print() 
