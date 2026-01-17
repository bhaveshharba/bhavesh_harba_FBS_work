from MainPage import Main

class Staff(Main):

    def staff_login():
        try:
            with open("StaffData.txt", "r") as file:
                staff_list = file.readlines()
        except FileNotFoundError:
            print("\nNo staff registered yet.\n")
            return

        username = input("Enter Staff Username: ")
        password = input("Enter Staff Password: ")

        for line in staff_list:
            sid, uname, pwd = line.strip().split(", ")

            if username == uname and password == pwd:
                print("\n Staff Login Successful\n")
                Main.staff_menu()
                return

        print("\n Invalid Staff Username or Password\n")
