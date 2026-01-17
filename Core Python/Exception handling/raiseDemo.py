from userException import UserException


def emp (id,name,age):
    if(not(age > 0 and age < 121)):
        raise UserException(age)
        # raise f'{age} is an invalid age.'         #will raise typeError

    print('ID:',id)
    print('Name :', name)
    print('Age :', age)

id = int(input('Enter id :'))
nm = input('Enter name :')
age = int(input('Enter age :'))

emp(id,nm,age)
