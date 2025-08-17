# 4. Write a program to check if given number is Armstrong number or not.
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
# 4*4*4*4)

num=int(input("enter number : "))
temp=num
count=0
temp2=0
temp3=0
temp4=0
while(temp>0):
    d=temp%10
    # print(f'{d}')
    temp=temp//10
    temp2=temp2+d*d*d
    temp3=temp3+d*d*d*d
    temp4=temp4+d*d*d*d*d

if(num==temp2):
    print(f'{num} is armstrong number ')
elif(num==temp3):
    print(f'{num} is armstrong number ')
elif(num==temp4):
    print(f'{num} is armstrong number ')
else:
    print(f'{num} is not armstrong number ')