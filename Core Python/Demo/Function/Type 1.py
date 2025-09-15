##WAP to check no is even or odd using function
#Without Passing Parameter
#Without Returning Value

def evenodd():
    num = int(input('Enter number to check even or odd :'))
    if (num==0):
        print(f'Number is Zero')
    elif(num%2==0):
        print(f'{num} is an even number.')
    else:
        print(f'{num} is an odd number.')

evenodd()