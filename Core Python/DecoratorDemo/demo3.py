# def fun():
#     print(x)

# x = 10
# fun()
# print(id(x))

def fun():
    x = 20      #x will be different variable
    print(id(x))

x = 10
print(id(x))
fun()
print(x)