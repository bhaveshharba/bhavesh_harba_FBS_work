try :
    li =[10, 20, 30, 40]
    print(li)
    ind = int(input('Enter index to pop the element :'))
    li.pop(ind)
    print(li)
    ele = int(input('Enter value to check index :'))
    print('Index', li.index(ele))
    del li
    print(li)               #NameError occured (except block execute)
except IndexError as e:                 #alias name for highlighting error type
    print('Index error :', e)               
except ValueError:
    print('Value error is occured.')
except Exception as e:         
    print('Error :', e)


