def add(x,y):
    print(x + y)

# add(10,20)

# demo = add
# demo (10, 20)

demo = add
del add
# add(10,20)      #Error
demo(10,20)
