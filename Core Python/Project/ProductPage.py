class Product:
    def __init__(self,product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
         return f'{self.product_id}, {self.name}, {self.price}, {self.quantity}'
    


if(__name__ == '__main__'):    
    p1 = Product(101, 'Laptop', 50000, 2)
    print(p1)
 