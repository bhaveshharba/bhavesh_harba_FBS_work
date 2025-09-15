# WAP to print following patterns :

def pattern(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(i == 1  or i == n or j + i == n ):
                print('*',end = ' ')
            else:
                print(' ',end=' ')
        print()         


n=int (input('Enter number :'))

pattern(n)