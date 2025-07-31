# 3. Write a program to accept distance in km and convert it into meters and
# centimeters both.

km = float(input('Enter Distance in KM :'))
m = km*1000
cm = km*100000

print(f'{km}KM is  {m} meters and {cm} centimeters')