import datetime

n = datetime.datetime.now()
# # print(type(n))
# print(n)

t = datetime.date.today()
# print(t)

# print(datetime.datetime.strftime(n, "%d-%m-%Y %H:%M:%S"))

print(n + datetime.timedelta(7))
print(n + datetime.timedelta(7, hours=1))
print(t + datetime.timedelta(7))


str = '31-10-2025'
print(type(str))
print(datetime.datetime.strptime(str, "%d-%m-%Y"))