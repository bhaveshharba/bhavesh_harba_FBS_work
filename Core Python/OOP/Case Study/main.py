from empManage import Empmanage


def login():
    userid = 'user'
    password = '1234'
    uname = input('Enter username :')
    passw = input('Enter password :')

    if(uname == userid and passw == password):
        print('Logged in successful...')
        ch = 0
        while(ch != '6'):
            print('''Please select option from below :
                1. Add employee
                2. Update employee
                3. Delete employee
                4. Show all employee
                5. Search employee
                6. Exit ''')
            
            ch = input('Enter choice :')
            
            if (ch == '1'):
                Empmanage.addEmp()
            elif(ch == '2'):
                Empmanage.updEmp()
            elif(ch == '3'):
                Empmanage.delEmp()
            elif(ch == '4'):
                Empmanage.showAllEmp()
            elif(ch == '5'):
                Empmanage.searchEmp()
            elif(ch == '6'):
                Empmanage.delEmp()
            else:
                print('Invalid choice...')


    else:
        print('Invalid credentials!.')


ch = 0
while(ch != '2'):
    print('''Please select option from below :
    1. Login
    2. Exit''')
    
    ch = input('Enter choice :')
    if(ch == '1'):
        login()
    elif(ch == '2'):
        print('Thank you!.')
    else:
        print('Invalid choise .....')


