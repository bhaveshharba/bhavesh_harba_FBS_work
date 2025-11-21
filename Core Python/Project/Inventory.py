from ProductPage import Product
from SalesPage import Sales
from prettytable import PrettyTable

class inventory(Product, Sales):


    def __init__(self):
        self.products = self.load_inventory()

    def load_inventory(self):
        products = {}
        try:
            with open('InventoryData.txt', 'r') as file:
                for line in file:
                    pid, name, price, quantity = line.strip().split(', ')
                    products[pid] = Product(pid, name, float(price), int(quantity))
        except FileNotFoundError as e:
            print('Error',e)
        return products
    


    def add_product(self):
        pid = (input('\nEnter Product ID :')).upper()
        if(pid in self.products):
            print('Product id alreday exists !!!!!!')
            return
        
        name = input('Enter Product Name :')
        price = float(input('Enter Product Price :'))
        quantity = int(input('Enter Quantity :'))

        self.products[pid] = Product(pid, name, price, quantity)

        print(f'\nProduct {name} Added Successfully!')


    def view_product(self):
        table = PrettyTable()
        table.field_names = ['Product_ID,', 'Name', 'Price', 'Quantity']

        if(not self.products):
            print('\nNo Product Available.')
            return
        print('\n===========Current Inventory==========')
        for Product_data in self.products.values():
            if(Product_data.quantity > 0):
                # print(Product_data)
                table.add_row([Product_data.product_id, Product_data.name, Product_data.price, Product_data.quantity])
        print(table)



    def search_product(self):
        pid = input('\nEnter Product ID to Search :').upper()
        if (pid in self.products):
            print(f'Found : {self.products[pid]}')
        else:
            print('\nProduct Not Found.')

    
    def update_product(self):
        pid = input('\nEnter Product ID to Update :')
        if (pid in self.products):
            product_data = self.products[pid]
            print('\n------Select Choice------')
            print('1.Update Price')
            print('2.Update Quantity')

            choice = input('Enter Choice :')

            if(choice == '1'):
                product_data.price = float(input('Enter new price :'))
                print('\n---Price Updated Successfully.---')
            elif(choice =='2'):
                product_data.quantity = int(input('Enter new quantity :'))
                print('\n---Quantity Updated Successfully.---')
            else:
                print('\n-----Invalid Choice.----')

        else:
            print('\nProduct Not Found.')

    def delete_product(self):
        pid = input('\nEnter Product ID to Delete :')
        if (pid in self.products):
            del self.products[pid]
            print('\n---Product Deleted Successfully.---')
        else:
            print('\nProduct not found.')
          

    def sell_product(self,sales_obj):
        pid = input('\nEnter Product ID to Sell :')
        if (pid not in self.products):
            print('\nProduct Not Found.')
            return
        
        product_data = self.products[pid]

        print(f'Selected : {product_data.name}, Price : Rs.{product_data.price}, Stock : {product_data.quantity}')
        qty = int(input('Enter quantity to sell :'))

        if (qty > product_data.quantity):
            print('\n---Not enough stock.---')
            return
        
        total_price = product_data.price * qty
        product_data.quantity -= qty

        sales_obj.record_sale(product_data.name, qty, total_price)

        print(f'Sold {qty} {product_data.name} for RS.{total_price}')

    
    def save_inventory(self):
        with open('InventoryData.txt', 'w') as file:
            for pid, prod in self.products.items():
                file.write(f'{pid}, {prod.name}, {prod.price}, {prod.quantity}\n')



 
if(__name__ == '__main__'):
    i1 = inventory()
    # i1.add_product()
    # i1.view_product()
    # # # i1.search_product()
    # # i1.update_product()
    # # # i1.delete_product()
    # i1.sell_product()
    # i1.save_inventory()
    # i1.view_product()