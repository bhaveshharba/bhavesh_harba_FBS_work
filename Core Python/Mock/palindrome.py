def palindrome(num):
    temp = num
    rev = 0
    while(temp>0):
        d = temp % 10
        rev = rev * 10 + d
        temp = temp // 10

    if(rev == num ):
        print('Number is palindrome ')
    else:
        print('Number is not palindrome')


num = int(input('Enter number :'))
palindrome(num)