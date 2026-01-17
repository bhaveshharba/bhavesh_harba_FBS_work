def numbers(num):
    for i in range(1,num + 1):
        yield i

res = numbers(100)
# print(res)

# for val in res:
#     print(val)

print(next(res))

print(next(res))
print(next(res))
print(next(res))    

# note:-
# for infinite value use while 
#Homework : Generate infinite prime number using generator
