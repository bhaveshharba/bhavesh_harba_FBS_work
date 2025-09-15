# 2. Python Program to Remove the nth Index Character from a Non-Empty
# String

string = input("Enter a non-empty string: ")
n = int(input("Enter the index of the character to remove: "))
result = ""

i = 0
while (i < len(string)):
    if (i != n):
        result += string[i]
    i += 1

print("String after removing character at index", n, ":", result)
