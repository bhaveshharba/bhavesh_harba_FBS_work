num= int(input('Enter number :'))

if(num>0):
    if(num>50):
        if(num>100):
            if(num>150):
                if(num>200):
                    if(num>500):
                        print('Number is Greater than 500')
                    else:
                        print('Number is Greater than 200 but less than 500')
                else:
                    print('Number is Greater than 150 but less than 200')
            else:
                print('Number is Greater than 100 but less than 150')
        else:
            print('Number is Greater than 50 but less than 100')
    else:
        print('Number is Greater than 0 but Less than 50')
else:
    print('Number is less than 0.')