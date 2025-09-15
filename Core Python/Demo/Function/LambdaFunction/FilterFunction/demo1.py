numbers = [0,23,45,36,87,95,34,65]

res = list(filter(lambda x : x ** 2 , numbers))
res = list(filter(lambda x : x % 2 == 0, numbers))
print(res)