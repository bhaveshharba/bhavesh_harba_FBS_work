# 11. WAP to check if given number Strong Number.

num = int(input('Enter Number  :'))
temp = num
sum = 0


while(temp>0):
    d = temp % 10
    temp = temp // 10 
    i=1
    fact = 1
    while(i<=d):
        fact *= i
        i += 1
    # print(fact)
    sum += fact

if(sum==num):
    print(f'{num} is Strong Number')
else:
    print(f'{num} is Not Strong Number')