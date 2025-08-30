# 3. Write a program to reverse a given number using recursive function.

def rev_num(num):
    temp = num
    while(temp>0):
        d = temp % 10
        temp = temp // 10
        print (d,end='')


num = int(input('Enter number :'))
res = rev_num(num)
print(f'{res}')