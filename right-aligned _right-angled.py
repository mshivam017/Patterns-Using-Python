row = int(input("Enter Row: "))
col = int(input("Enter Col: "))
for i in range(0, row):
    for j in range(0, col):
        if j <= (row-1)-i:
            print('*|', end=' ')
        else:
            print(' ', end='')
    print()
        