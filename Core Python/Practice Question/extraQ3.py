# 3. Find greatest number from  three number using nested if else

#Using Nested If else

num1 = int(input('Enter First number :'))
num2 = int(input('Enter Second number :'))
num3 = int(input('Enter third number :'))

if(num1>num2):
   if(num1>num3):
      print(f'{num1} is Greatest Number.')
   else:
      print(f'{num3} is Greatest Number.')
else:
    if(num2>num3):
      print(f'{num2} is Greater Number.')
    else:
      print(f'{num3} is Greater Number.')
   
