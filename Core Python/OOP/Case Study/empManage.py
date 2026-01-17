from dev import Dev
from hr import hr
from admin import admin

class Empmanage :
    emp_detail = {}

    def addEmp():
        id = input('Enter id :')
        nm = input('Enter name :')
        basic = input('Enter basic sal :')
        ch = 0
        
        print('''Please select dept :
        1. S/W devloper
        2. Hr n   
        3. Admin''')
        ch = input('Enter choice :')
        if(ch == '1'):
            bonus = float(input('Enter bonus :'))
            d1 = Dev(id, nm, basic, bonus)
            d1.calSal()
            eData = str(d1)


        elif(ch == '2'):
            comm = float(input('Enter Commision :'))
            h1 = hr(id, nm, basic, comm)
            h1.calSal()
            eData = str(h1)
        

        elif(ch == '3'):
            allowance = float(input('Enter allowance :'))
            a1 = admin(id, nm, basic, allowance)
            a1.calSal()
            eData = str(a1)
        
        Empmanage.emp_detail[id] = eData
        print('Employee added successfully')

    def updEmp():
        pass
    def delEmp():
        pass
    def showAllEmp():
        print(Empmanage.emp_detail)
    def searchEmp():
        pass

