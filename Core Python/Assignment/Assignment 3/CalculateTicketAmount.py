# 11. Accept age of five people and also per person ticket amount and then calculate total
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.


age1 = int(input('Enter age of First Person :'))
age2 = int(input('Enter age of Second Person :'))
age3 = int(input('Enter age of Third Person :'))
age4 = int(input('Enter age of Fourth Person :'))
age5 = int(input('Enter age of Fifth Person :'))

ticket_amt = int(input('Enter Ticket Amount :'))
total_amt=0

# First Person

if(age1<12):
    dis_amt= ticket_amt * 0.3
    total_amt1= ticket_amt - dis_amt
elif(age1>59):
    dis_amt= ticket_amt * 0.5
    total_amt1= ticket_amt - dis_amt
else:
    total_amt1=ticket_amt

# Second Person

if(age2<12):
    dis_amt= ticket_amt * 0.3
    total_amt2= ticket_amt - dis_amt
elif(age2>59):
    dis_amt= ticket_amt * 0.5
    total_amt2= ticket_amt - dis_amt
else:
    total_amt2=ticket_amt

# Third Person

if(age3<12):
    dis_amt= ticket_amt * 0.3
    total_amt3= ticket_amt - dis_amt
elif(age3>59):
    dis_amt= ticket_amt * 0.5
    total_amt3= ticket_amt - dis_amt
else:
    total_amt3=ticket_amt

# Fourth Person

if(age4<12):
    dis_amt= ticket_amt * 0.3
    total_amt4= ticket_amt - dis_amt
elif(age4>59):
    dis_amt= ticket_amt * 0.5
    total_amt4= ticket_amt - dis_amt
else:
    total_amt4=ticket_amt

# Fifth Person

if(age5<12):
    dis_amt= ticket_amt * 0.3
    total_amt5= ticket_amt - dis_amt
elif(age5>59):
    dis_amt= ticket_amt * 0.5
    total_amt5= ticket_amt - dis_amt
else:
    total_amt5=ticket_amt
    
total_amt=(total_amt1 + total_amt2 + total_amt3 + total_amt4 + total_amt5)
print(f'Total Amount of Ticket is {total_amt}')