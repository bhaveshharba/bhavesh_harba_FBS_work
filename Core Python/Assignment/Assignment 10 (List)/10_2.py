# 2. Write a program to find maximum and minimum element in a list.


li=[10,20,45,90,76,105]

max = li[0]

for i in range(1,len(li)):
    if (li[i]> max):
        max = li[i]

min = li[0]
for i in range(1,len(li)):
    if(li[i]<min):
        min = li[i]
        

print('Maximum number is ',max)
print('Minimum number is ',min)