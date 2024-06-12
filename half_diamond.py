row = int(input("Enter Row: "))
col = row
for i in range(row):
    for j in range(col):
        if j<=i:
            print("*", end='')
        else:
            print(' ', end='')
    print()

for i in range(1,row):
    for j in range(col):
        if j<=(row-1)-i:
            print('*', end='')
        else:
            print(' ', end='')
    print()
