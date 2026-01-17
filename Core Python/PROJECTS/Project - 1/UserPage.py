from AdminPage import Admin
from StaffPage import Staff

class user(Admin):
    def user():
        
        print("===== INVENTORY MANAGEMENT SYSTEM =====")
        
        print("1. Admin Login")
        print("2. Staff Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            Admin.admin_login()
        elif choice == "2":
            Staff.staff_login()
        elif choice == "3":
            print("Thank you!")
        else:
            print("Invalid option!\n")

    user()