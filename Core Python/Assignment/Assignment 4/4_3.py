# 3. WAP to print sum of series upto n.

n = int(input("Enter the value of n: "))
sum = 0

for i in range(1, n + 1):
    sum += i

print(f'Sum of the series up to, {n}, is :, {sum} ')
