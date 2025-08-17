# 1. Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# # times. After that program to terminate.


for i in range(1,3+1):
    uid = (input('Enter User ID :'))
    pas = int(input('Enter Password :'))
    if ((uid=='admin')and(pas==1234)):
        print('ID and Password is Correct')
        break
    else:
        print ('Incorrect ID and Password ')
    print()