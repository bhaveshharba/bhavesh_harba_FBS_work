# ABCDE
# BCDE
# CDE
# DE
# E


for i in range(1,6):
    for j in range(i,6):
        print(chr(64+j), end='')
    print()