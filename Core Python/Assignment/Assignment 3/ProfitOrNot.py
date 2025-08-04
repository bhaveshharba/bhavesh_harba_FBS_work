# 6. Write a program to calculate profit or loss.

cp = int(input('Enter Cost Price Of Product :'))
sp = int(input('Enter Selling Price of Product :'))

if(cp<sp):
    print('Profit')
elif(sp>cp):
    print('Loss')
elif(cp==sp):
    print('No Profit No Loss')