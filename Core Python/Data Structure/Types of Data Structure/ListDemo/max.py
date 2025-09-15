# Find max from number.

li=[10,20,45,90,76,105]

max = li[0]
for i in range(1,len(li)):
    if (li[i]> max):
        max = li[i]

print('Maximum number is ',max)