# 8. Write a program to prompt user to enter userid and password. After verifying
# userid and password display a 4 digit random number and ask user to enter the
# same. If user enters the same number then show him success message otherwise
# # failed. (Something like captcha)


import random
captcha = random.randint(1111,9999)

uid = (input('Enter User ID :'))
pas = int(input('Enter Password :'))

if(uid=='Admin' and pas==12345):
    print('Valid User ID and Password.')
    print(f'{captcha} CAPTCHA ')
    u_captch = int(input('Enter Captcha :'))
    if(captcha ==  u_captch):
        print('Successful.')
    else:
        print('Invalid Captcha.')
else:
    print('Invalid User ID and Password.')
