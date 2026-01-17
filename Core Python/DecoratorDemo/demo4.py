def mydecorator(fun):
    def wrapper():
        print('This is wrapper function')
        fun()
        print('this is end')
    return wrapper


@mydecorator
def greet():
    print('Good morning')

greet()