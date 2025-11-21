from UserPage import user
from Inventory import inventory
from SalesPage import Sales

def main():

    role = user.login()
    print(f'\n{role}')

    if not role:
        return f'Login Fail'
    
    Inventory = inventory()
    sales = Sales()
    
    while True:
        print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
        
        if role == "admin":
            print("1. Add Product")
            print("2. View Inventory")
            print("3. Search Product")
            print("4. Update Product")
            print("5. Delete Product")
            print("6. Sell Product")
            print("7. View Sales Report")
            print("8. SAVE AND EXIT")
    
        elif role == "staff":
            print("1. View Inventory")
            print("2. Sell Product")
            print("3. View Sales Report")
            print("4. SAVE AND LOG OUT")

        choice = input('\nEnter choice :')
        
        if(role == "admin"):
            if(choice == '1'):
                Inventory.add_product()                #Done
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
                Inventory.save_inventory()
                sales.save_sales()  
                print('\n----------Logging Out----------')
                break
            else:
                print('\n----------Invalid Choice----------')

        elif(role == 'staff'):
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
                break
            else:
                print('\n----------Invalid Choice----------')



if(__name__ =='__main__'):
    main() 