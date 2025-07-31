# 2. Write a program to calculate simple interest based on Principal, Rate and Time
# (SI = P*R*T/100)

p = float(input('Enter Principle Amount :'))
r = float(input('Enter Rate :'))
t = float(input('Enter Time :'))

si= ((p*r*t)/100)

print(f'Simple Interest is {si}.')
