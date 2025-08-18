# 5. WAP to calculate selling price of book based on cost price and discount.

cp = float(input('Enter Cost Price of Book :'))
dp = float(input('Enter Disscount in percentage % :'))

da = cp * dp/100

sp = cp+da

print(f'Selling price of Book is {sp}')