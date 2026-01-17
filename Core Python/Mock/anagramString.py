# # str1 = 'listen'
# # str2 = 'silent'

# count1 = 0
# count2 = 0

# for ch in str1:
#     count1 += 1

# for ch in str2:
#     count2 += 1

# if(count1 != count2):
#     print('String is not anagram.')
# else: 
#     dict1 = {}
#     dict2 = {}

#     for ch in str1:
#         if (ch in dict1):
#             dict1[ch] += 1
#         else:
#             dict1[ch] = 1

#     for ch in str2:
#         if (ch in dict2):
#             dict2[ch] += 1
#         else:
#             dict2[ch] = 1

#     if(dict1 != dict2):
#         print('String is not an anagram string.')
#     else:
#         print('String is an anagram string.')

def Anagram_string(str1, str2):
    
    count1 = 0
    count2 = 0

    for ch in str1:
        count1 += 1

    for ch in str2:
        count2 += 1

    if(count1 != count2):
        print('String is not anagram.')
    else: 
        dict1 = {}
        dict2 = {}

        for ch in str1:
            if (ch in dict1):
                dict1[ch] += 1
            else:
                dict1[ch] = 1

        for ch in str2:
            if (ch in dict2):
                dict2[ch] += 1
            else:
                dict2[ch] = 1

        if(dict1 != dict2):
            print('String is not an anagram string.')
        else:
            print('String is an anagram string.')

str1 = input('Enter string 1:')
str2 = input('Enter string 2:')

Anagram_string(str1,str2)
