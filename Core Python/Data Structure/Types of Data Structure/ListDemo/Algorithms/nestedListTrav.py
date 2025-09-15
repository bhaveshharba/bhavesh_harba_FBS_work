li =[[10,20,30],[40,50,60]]
sum =0
for i in range(0,len(li)):
    for j in range(0,len(li[i])):
        sum += li[i][j]
print(sum)