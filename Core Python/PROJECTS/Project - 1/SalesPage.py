from datetime import datetime
from prettytable import PrettyTable

class Sales :

    def __init__(self):
        self.sales_record = self.load_sales()

    
    def load_sales(self):
        sales = []
        try :
            with open('SalesData.txt','r') as file:
                for line in file :
                    date, product, qty, total = line.strip().split(', ')
                    sales.append({
                        "date": date,
                        "product" : product,
                        "quantity" : int(qty),
                        "total_price" : float(total)   
                    })
        except FileNotFoundError as e:
            print('Error :', e)
        return sales
     
     
    def record_sale(self, product_name, quantity, total_price):
        data = {
            "product": product_name,
            "quantity": quantity,
            "total_price": total_price,
            "date": datetime.now().strftime("%d-%m-%Y|%H:%M:%S")
        }
        self.sales_record.append(data)
        print(f'Sale recorded: {product_name} x {quantity} = ₹{total_price}')



    def save_sales(self):
        with open('SalesData.txt','w') as file:
            for data in self.sales_record:
                file.write(f'{data['date']}, {data['product']}, {data['quantity']}, {data['total_price']}\n')                



    def view_sales(self):  
        if not self.sales_record:
            print("No sales.")
            return
        print("\n--- Sales Report ---")
        table = PrettyTable()
        table.field_names = ['Date & Time', 'Product Name', 'Quantity', 'Total Price']
        total = 0
        for data in self.sales_record:
            # print(f"{data['date']} | {data['product']} | {data['quantity']} | ₹{data['total_price']}")
            table.add_row([data['date'], data['product'], data['quantity'], data['total_price']])
            total += data['total_price']
        print(table)
        print(f"\nTotal Revenue: ₹{total}")


    

# if(__name__ == '__main__'):
#     s1 = Sales()
#     s1.view_sales()
# # # s1.save_sales()