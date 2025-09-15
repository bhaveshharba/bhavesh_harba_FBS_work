# WAP to Print pattern
# AAAAA
# BBBBB
# CCCCC
# DDDDD
# EEEEE

for i in range(1,6):
    for j in range(1,6):
        print(chr(64 + i),end='')
    print()  