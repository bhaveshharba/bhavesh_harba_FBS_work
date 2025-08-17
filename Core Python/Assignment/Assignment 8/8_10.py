# 10. Write a program to check if entered year is a leap year or not.

def leap_year(y):
    if(y % 4 == 0):
        if(y % 100 == 0):
            if( y % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False


year = int(input('Enter Year to check :'))
result = leap_year(year)

if(result):
    print(f'{year} is leap year.')
else:
    print(f'{year} is not leap year.')
