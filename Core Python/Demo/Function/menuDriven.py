def evenOdd(num):
    if(num == 0):
        return f'{num} is neutral'
    elif(num % 2 == 0):
        return f'{num} is an even number.'
    else:
        return f'{num} is an odd number.'
    
def positive_negative(num):
    if(num == 0):
        return f'{num} number is Zero'
    elif(num > 0 ):
        return f'{num} is Positive Number'
    else:
        return f'{num} is Negative Number'
    
def CheckPrime(num):
    for i in range(2,num // 2+1):
        if (num % i == 0):
            return False
    else:
        return True
    
def CheckPerfect(num):
    sum = 0
    if(num<=0):
        return False
    else:
        for i in range(1,num):
            if (num % i == 0):
                sum += i
        return sum

def CheckStrong(num):
    temp = num
    sum = 0
    while(temp>0):
        d = temp % 10
        temp = temp // 10
        i = 1
        fact = 1
        while(i <= d):
            fact *= i
            i += 1
        sum += fact
    return sum
    



ch = 0
while(ch != '8'):
    print('''Please select choice from below :
          1. Check even odd
          2. Check positive negative
          3. Prime or not
          4. Perfect No
          5. Strong No
          6. Armstrong No
          7. Palindrome No
          8. Exit...... ''')
    ch = input('Enter Choice :')
    if(ch == '1'):
        num = int(input('Enter number to check :'))
        res = evenOdd(num)
        print(res)

    elif(ch == '2'):
        num = int(input('Enter number to check :'))
        res = positive_negative(num)
        print(res)

    elif(ch == '3'):
        num = int(input('Enter number to check :'))
        res = CheckPrime(num)
        if(res):
            print(f'{num} is a prime number .')
        else:
            print(f'{num} is not a prime number.')

    elif(ch == '4'):
        num = int(input('Enter number to chek :'))
        res = CheckPerfect(num)
        if(res == num):
            print(f'{num} is Perfect Number.')
        else:
            print(f'{num} is not Perfect Number.')

    elif(ch == '5'):
        num = int(input('Enter Number to check :'))
        res = CheckStrong(num)
        if(res == num):
            print(f'{num} is Strong Number.')
        else:
            print(f'{num} is not Strong Number.')

    elif(ch == '6'):
        pass
    elif(ch == '7'):
        pass
    elif(ch == '8'):
        print('Thank You !')
    else:
        print('####Invalid Choice.####')





# # Armstrong No
# # Palindrome No






