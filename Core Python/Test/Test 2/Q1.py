# 1. Write a program to accept year from user and check if it is a leap year or not.

year = int(input('Enter Year to check :'))

if(year % 4 == 0):
    if(year % 100 == 0):
        if( year % 400 == 0):
             print(f'{year} is Leap Year.')
        else:
            print(f'{year} is Not Leap Year.')
    else:
        print(f'{year} is Leap Year.')
else:
    print(f'{year} is Not Leap Year.')


