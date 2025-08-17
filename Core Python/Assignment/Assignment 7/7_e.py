#      1
#     1 2
#    1   3
#   1     4
#  1 2 3 4 5


for i in range(1,6):
    for j in range(1,6-i):
     print('',end= ' ')
    for j in range(1,i+1):
        if(i==3 and j==2):
          print('  ',end = '')
        elif(i==4 and j==2):
            print('   ',end = '')
        elif(i==4 and j==3):
            print(' ',end ='')
        else:
            print(f' {j}',end ='')
    print()