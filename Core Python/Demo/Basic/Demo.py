user_id=int(input("enter user id = "))
password=input("enter password = ")

print("re-enter user id and password")

for i in range(1,3+1):
    t1=int(input("enter user id = "))
    t2=input("enter password = ")
    if(t1==user_id and t2==password):
        print("the user id and password is correct")
        break
    else:
        print("the user id and password is incorrect")
print("aman")