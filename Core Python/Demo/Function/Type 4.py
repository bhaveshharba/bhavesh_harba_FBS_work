#With passing parameter (with i/p)
#With returnig value(with o/p)

def checkPrime(num):
    for i in range(2,num // 2+1):
        if (num % i == 0):
            return False
    else:
        return True
    

num = int(input('Enter Number:'))
res = checkPrime(num)
if(res):
    print(f'{num} is Prime Number')
else:
    print(f'{num} is Not Prime Number')