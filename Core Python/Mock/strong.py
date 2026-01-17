# # Strong No       145 = 1! + 4! + 5!

def Strong_num(num):
    temp = num
    sum = 0

    while(temp>0):
        d = temp % 10
        temp = temp // 10
        i = 1
        Fact = 1
        while(i<=d):
            Fact *= i
            i += 1
        sum += Fact

    if (sum == num):
        print('No is strong no')
    else:
        print('No is no strong no')


num = int(input('Enter Number :'))
Strong_num(num)