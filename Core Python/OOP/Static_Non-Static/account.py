## Static Variable

class Account :
    branch_name = 'BOI FC road, pune.'              #static variable
    ifsc_code = 'BKI000082'                         #static variable

    def __init__(self,holder_nm,acc_no,bal):
        self.holder_name = holder_nm
        self.acc_no = acc_no
        self.bal = bal

    def display(self):
        print('Branch name :',Account.branch_name)
        print('IFSC code :',Account.ifsc_code)
        print('Holder Name :',self.holder_name)
        print('Acc No :',self.acc_no)
        print('Balance :',self.bal)
        print('####################################')


holder_name = input('Enter holder name :')
acc_no = input('Enter Account no :')
bal = input('Enter balance :')

ac1 = Account(holder_name,acc_no,bal)
ac1.display()

# ac2 = Account('XYZ',67890,10000)
# ac2.display()
        