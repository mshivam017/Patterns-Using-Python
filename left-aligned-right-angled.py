row = int(input("Enter Row: "))
col = int(input("Enter Col: "))

for i in range(0, row):
    for j in range(0, col):
        if j >= i:
            print('*', end='')
        else:
            print(' ', end='')
    print()