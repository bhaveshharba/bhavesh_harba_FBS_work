class user:
    def login():
        for i in range(1, 3+1):
            username = input('Enter username :')
            password = int(input('Enter Password :'))
            if ((username == 'admin' and password == 1234) or (username == 'staff' and password == 4321) ):
                print('\n----------Login successfully----------\n')
                return username
            else:
                print('----------Incorrect ID - Password !----------')
                # return None
        print('Please try again later !')
