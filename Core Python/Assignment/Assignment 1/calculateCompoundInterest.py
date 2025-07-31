# 5 Write a program to enter P,T,R and calculate Compound Interest.

p = float(input('Enter Principle Amount:'))
r = float(input('Enter Rate :'))
t = float(input('Enter Duration :'))

a = p*(1+r/100)**t
ci = a-p

print(f'Compound Interest is {ci}')