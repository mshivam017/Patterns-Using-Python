row = int(input("Enter Row: "))
col = 2 * row - 1  # To make the pattern centered

for i in range(row):
    for j in range(col):
        if j<= (row-1)+i and j>= (row-1)-i:
            print('*', end='')
        else:
            print(' ', end='')
    print()
