# 28    = 1 + 2 + 4 + 7 + 14
# perfect no = sum of its proper divisor



def perfect_no(num):
    sum = 0 
    if (num <0 ):
        print('Number is zero')
    else:
        for i in range(1,num):
            if (num % i == 0):
                sum += i
        print(sum)

    if (sum == num):
        print('Number is perfect.')
    else:
        print('Number is not perfect.')

num = int (input('eter no '))
perfect_no(num)