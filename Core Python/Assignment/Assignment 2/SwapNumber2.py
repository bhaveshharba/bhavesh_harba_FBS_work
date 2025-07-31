# 9. Write a program to swap two numbers without using third variable.
x = int(input('Enter value of x :'))
y = int(input('Enter value of y :'))

x=x+y
y=x-y
x=x-y

# x,y=y,x         ##Python shortcut

print(f'x {x},\ny {y}.')
 
