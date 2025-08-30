# 10. Write a program to reverse a number using recursion.

def rev_num(n):
    temp = n
    while(temp>0):
        d = temp % 10
        rev_num(n//10)
        print(d)


num = int ('Enter number :')
res = rev_num(num)
print(res)