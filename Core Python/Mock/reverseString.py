# def rev_string(str):
#     i = len(str)-1
#     print(i)
#     result =''
#     while(i>=0):
#         result += str[i]
#         i -= 1
#     print (result)

# rev_string(str)


str = input('Enter string :')


def rev_str(str):
    rev = ''
    for ch in str:
        rev = ch + rev
    
    print(rev)

rev_str(str)