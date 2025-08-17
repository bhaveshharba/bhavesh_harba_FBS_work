#   3. Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

total_amount=0
temp1=0
temp2=0
temp3=0
temp4=0
i=0
print("Children below 12 = '30%' discount")
print("Senior citizen (above 59) = '50%' discount")

n=int(input("no. of passenger : "))
t=int(input("ticket cost : "))

while(i<n):
    age=float(input("age : "))
    if(age>=12 and age<=59):
        ticket_100=t
        temp3=t
        # print(temp3)
    elif(age>=59):
        ticket_60=t/100*50
        temp2=t-ticket_60
        # print(temp2)
    elif(age<=12):
        ticket_30=t/100*30
        temp1=t-ticket_30
        # print(temp1)
    temp4=temp4+t
    i=i+1
total_amount=temp1+temp2+temp3

print(f'total price of ticket to travel {temp4}')
print(f'total amount of ticket to travel with discount : {total_amount}')
