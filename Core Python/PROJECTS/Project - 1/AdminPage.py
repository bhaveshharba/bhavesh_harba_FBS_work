from MainPage import Main

class Admin(Main):
    def admin_login():
        username = "admin"
        password = "1234"

        u = input("Enter admin username: ")
        p = input("Enter admin password: ")

        if u == username and p == password:
            print("\nLogin successful!\n")
            Main.admin_menu()
        else:
            print("\nInvalid login!\n")

    def add_staff():
        staff_id = input("Enter Staff ID: ").upper()
        name = input("Enter Staff Username: ")
        password = input("Enter Password: ")

        with open("StaffData.txt", "a") as file:
            file.write(f"{staff_id}, {name}, {password}\n")

        print("\n✅ Staff Added Successfully!\n")
    
    def view_staff():
        try:
            with open("StaffData.txt", "r") as file:
                data = file.readlines()
        except FileNotFoundError:
            print("\nNo staff available.\n")
            return

        print("\n------ STAFF LIST ------")
        for line in data:
            sid, name, pwd = line.strip().split(", ")
            print(f"Staff ID : {sid}")
            print(f"Username : {name}")
            print("------------------------")