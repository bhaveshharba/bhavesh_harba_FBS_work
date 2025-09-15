# Find Greater Number from three numbers


# Using if else ladder

num1 = int(input('Enter First number :'))
num2 = int(input('Enter Second Number :'))
num3= int(input('Enter third Number :'))

if((num1 > num2) and (num1 > num3)):
    print(f'{num1} is Greater Number.')
elif((num2 > num1) and (num2 > num3)):
    print(f'{num2} is Greater Number.')
else:
    print(f'{num3} is Greater Number.')

# Using Nested If else

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