# 7. Program to Find the Roots of a Quadratic Equation

a = int(input('Enter value for a :'))
b = int(input('Enter Value for b :'))
c = int(input('Enter value for c :'))

sqrt = ((b**2)-(4*a*c))**0.5
res1 = ((-b+sqrt)/2*a)
res2 = ((-b-sqrt)/2*a)

print(f'result 1 {res1}')
print(f'result 2 {res2}')
