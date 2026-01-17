import time


t = time.time()
print(t)

print(time.ctime(t))

# print(time.sleep(3))
# print('Working....')

# print(time.localtime())

print(time.localtime().tm_mday)
