emp = {}

ch = 0
while(ch != '6'):
    print('''Please select option from below :
        1. Add employee
        2. Update employee
        3. Delete employee
        4. Search employee
        5. Show all employee
        6. Exit...
        ''' )
    ch = input('Enter choice :')

    if(ch == '1'):
        id = input('Enter eid :')
        name = input('Enter name :')
        sal = float(input('Enter salary :')) 
        # eData = ', '.join([id,name,sal])
        eData = f'{id},{name},{sal}'
        emp[id] = eData

    elif(ch == '2'):
        pass
    elif(ch == '3'):
        pass
    elif(ch == '4'):
        pass
    elif(ch == '5'):
        print(emp)
    elif(ch == '6'):
        print('Thank You')
    else:
        print('Invalid Option')