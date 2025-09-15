##Factorial of no
#Without passing parameter (with i/p)
#With returnig value (with o/p)

def fact():
    num= int(input('Enter number :'))
    fact=1
    for i in range(1,num+1):
        fact *= i
    return fact

res = fact()
print('Factorial is ', res)