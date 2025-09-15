#Find third max from number

li=[10,20,45,90,76,88,105]
max = li[0]
smax = 0
tmax = 0
for i in range(1,len(li)):
    if (li[i]> max):
        tmax = smax
        smax = max
        max = li[i]
    elif(li[i]>smax):
        tmax = smax
        smax = li[i]
    elif(li[i]> tmax):
        tmax = li[i]

print('Maximum number is ',max)
print('Second Maximum number is ',smax)
print('Third Maximum number is ',tmax)

