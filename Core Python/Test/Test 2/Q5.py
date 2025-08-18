# 5. A man goes for shopping. He buys 5 products. Accept the price of all products and display
# the total bill after adding 18% GST

prod1 = int(input('Enter Price of First Product :'))
prod2 = int(input('Enter Price of Second Product :'))
prod3 = int(input('Enter Price of Third Product :'))
prod4 = int(input('Enter Price of Fourth Product :'))
prod5 = int(input('Enter Price of Fifth Product :'))

amount = prod1+prod2+prod3+prod4+prod5
gst = amount * 18/100
total_amount = amount + gst
print (f'Total Bill include 18% GST is {total_amount}Rs.')