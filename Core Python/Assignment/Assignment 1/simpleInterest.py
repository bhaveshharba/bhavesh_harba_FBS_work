# 4. Write a program to enter P, T, R and calculate simple Interest.

p = float(input('Enter Principle Amount:'))
r = float(input('Enter Rate :'))
t = float(input('Enter Duration'))
si= (p*r*t)/100
print(f'Simple Interest is {si}.')

