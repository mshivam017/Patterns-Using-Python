ascii_val = 65
for i in range(1,6):
    for j in range(1,10):
        if j>=6-i and j<=4+i:
            print(chr(ascii_val), end='')
        else:
            print(' ', end='')
    ascii_val+=1
    print()