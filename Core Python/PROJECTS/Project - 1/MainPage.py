from Inventory import inventory
from SalesPage import Sales


class Main(inventory,Sales):

    def admin_menu():

        Inventory = inventory()
        sales = Sales()

        choice = 0
        while(choice != '10'):

            print("1. Add Product")
            print("2. View Inventory")
            print("3. Search Product")
            print("4. Update Product")
            print("5. Delete Product")
            print("6. Sell Product")
            print("7. View Sales Report")
            print("8. Add Staff")
            print("9. View Staff")
            print("10. SAVE AND EXIT")

            choice = input('\nEnter choice :')


            if(choice == '1'):
                Inventory.add_product()                 #Done
            elif(choice == '2'):
                Inventory.view_product()                #Done
            elif(choice == '3'):
                Inventory.search_product()              #Done
            elif(choice == '4'):
                Inventory.update_product()              #Done
            elif(choice == '5'):
                Inventory.delete_product()              #Done
            elif(choice == '6'):
                Inventory.sell_product(sales)           #Done
            elif(choice == '7'):
                sales.view_sales()                      #Done
            elif(choice == '8'):
                from AdminPage import Admin             # Import happens inside function, not at top --- to solve cirular import 
                Admin.add_staff()
            elif(choice == '9'):
                from AdminPage import Admin             # Import happens inside function, not at top --- to solve cirular import 
                Admin.view_staff()              
            elif(choice == '10'):
                Inventory.save_inventory()
                sales.save_sales()  
                print('\n----------Logging Out----------')           
            else:
                print('\n----------Invalid Choice----------')


    def staff_menu():

        Inventory = inventory()
        sales = Sales()
       
        choice = 0
        while(choice != '4'):

            print("1. View Inventory")
            print("2. Sell Product")
            print("3. View Sales Report")
            print("4. SAVE AND LOG OUT")

            choice = input('\nEnter choice :')

            if choice == "1":
                Inventory.view_product()                    #Done
            elif choice == "2":
                Inventory.sell_product(sales)               #Done
            elif choice == "3":
                sales.view_sales()                          #Done
            elif choice == "4":
                Inventory.save_inventory()                  #done
                sales.save_sales()  
                print('\n----------Logging Out----------')
            else:
                print('\n----------Invalid Choice----------')