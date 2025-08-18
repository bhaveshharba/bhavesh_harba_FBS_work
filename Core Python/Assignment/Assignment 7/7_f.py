#    1 2 3 4 5
#    1     5
#    1   5
#    1 5
#    1

# n = 4
# for i in range(1, n+2):
#     print(i, end=" ")
# print()
# spaces = (2 * (n-1)) - 1  
# for i in range(n-2):
#     print("1" + " " * (spaces - 2*i) + "5")
#     print("1 5")
# print("1")


for i in range(1,6):
    for j in range(1,7-i):
        if(j==1 or i==1 ):
            print(j,end=' ')
        elif(6-j==i):
            print('5', end=' ')
        else:
            print(' ', end=' ')
    print()

