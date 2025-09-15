li=[10,20,5,45,90,76,105,1]
min = li[0]

for i in range(1,len(li)):
    if (li[i]< min):
        min = li[i]

print('Minimum number is ', min)