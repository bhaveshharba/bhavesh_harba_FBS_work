# 3. Write a program to find the second largest element in the list.\

li=[10,20,45,90,76,105]
max = li[0]
smax = 0

for i in range(1,len(li)):
    if(li[i]>max):
        smax = max
        max = li[i]
    elif(li[i]>smax):
        smax = li[i]

print('Second largest element in list is :',smax)