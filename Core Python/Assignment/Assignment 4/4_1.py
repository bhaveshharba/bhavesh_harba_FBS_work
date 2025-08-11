# 1. WAP to print all even numbers until n.  


num = int (input('Enter Number :'))
i=1
while(i<=num):
    if(i % 2 == 0):
        print(i)
    i += 1