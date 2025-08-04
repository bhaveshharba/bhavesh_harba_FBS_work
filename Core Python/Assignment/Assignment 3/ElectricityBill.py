# 13. Write a program to input electricity unit charges and calculate total electricity bill
# according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill

unit = int(input('Enter Electricity Unit :'))
total_bill = 0

if (unit > 0):
    if(unit > 50):
        if(unit > 150):
            if(unit > 250):
                total_bill = 50 * 0.5
                unit2 = unit - 50
                total_bill2 = 100 * 0.75
                unit3 = unit2 - 100
                total_bill3 = 100 * 1.20
                unit4 = unit3 - 100
                total_bill = total_bill + total_bill2 + total_bill3 + (unit4 * 1.50)
            else:
                total_bill = 50 * 0.5
                unit2 = unit - 50
                total_bill2 = 100 * 0.75
                unit3 = unit2- 100
                total_bill = total_bill + total_bill2 + (unit3 * 1.20 )
        else:
            total_bill = 50 * 0.5
            unit2 = unit - 50
            total_bill= total_bill +(unit2 * 0.75)
    else:
        total_bill = unit * 0.5
else:
    print('Invalid Iniput.')

sur_charges = total_bill * 0.2
total_charges = total_bill + sur_charges


print(f'Total Electricity Charges is {total_charges} .')