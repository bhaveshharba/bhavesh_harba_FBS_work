# 7. Write a program to check if user has entered correct userid and password.

uid = (input('Enter user ID :'))
pas = int(input('Enter Password :'))

if((uid == 'Bhavesh') and (pas == 12345)):
    print('Valid ID Password.')
else:
    print('Invalid ID Password.')
