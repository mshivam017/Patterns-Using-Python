row = int(input('Enter Number of Rows: '))
col = row
ascii_val = 65
for i in range(1,row+1):
    for j in range(1,col+1):
        if j<=i:
            print(chr(ascii_val), end='')
        else:
            print(' ', end='')
    ascii_val = ascii_val+1
    print()