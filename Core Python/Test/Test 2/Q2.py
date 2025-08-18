# 2.Write a program to accept 3 digit number. If first digit is double of second digit and half of
# third digit then display “Yes, you have done it”, otherwise display “Please try next time”.
# Eg : - 428 , 214 etc.


num = int(input('Enter Number to check :'))
temp = num

d1= temp % 10
temp = temp // 10

d2= temp % 10
temp = temp // 10

d3= temp  % 10
temp = temp // 10


# print(f'{d3} {d2} {d1}')

if(d3 == d2*2) and (d3 == d1/2):
    print('Yes, You have done it.')
else:
    print('Please try next time.')
