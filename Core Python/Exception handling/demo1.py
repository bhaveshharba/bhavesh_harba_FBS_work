# Addition of two number
#1st option

try:
    num1 = int(input('Enter number 1 :'))
    num2 = int(input('Enter number 2 :'))
except:
    print('Invalid input ...')
else:
    sum = num1 + num2
    print(f'Addition of {num1} and {num2} is :{sum}')


#2nd option (write all code where you feel exception can occur in try block)

# try:
#     num1 = int(input('Enter number 1 :'))
#     num2 = int(input('Enter number 2 :'))
#     sum = num1 + num2
#     print(f'Addition of {num1} and {num2} is :{sum}')
# except:
#     print('Invalid input ...')
