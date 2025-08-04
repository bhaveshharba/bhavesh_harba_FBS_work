# 10. Write a program to check if person is eligible to marry or not (male age >=21 andfemale age>=18)

gender = str(input('Enter Gender (M/F) :'))
age = int(input('Enter age :'))

if((gender == 'M' and age>=20) or (gender == 'F' and age>=18) ):
    print("Eligible for marriage.")
else:
    print("Not Eligible for marriage.")
