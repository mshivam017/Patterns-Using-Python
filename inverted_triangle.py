row = int(input("Enter row:  "))
col = row*2-1 
for i in range(row):
    for j in range(col):
        if j>=i and j<=(col-1)-i:
            print('*', end='')
        else:
            print(' ', end='')
    print()