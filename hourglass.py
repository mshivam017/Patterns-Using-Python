row = int(input('Enter Row: '))
col = 2*row-1

for i in range(row):
    for j in range(col):
        if j>=i and j<=((col-1)-i):
            print('*', end='')
        else:
            print(' ', end='')
    print()  

for i in range(1,row):
    for j in range(col):
        if j<=(row-1)+i and j>=(row-1)-i :
            print('*', end='')
        else:
            print(' ',  end='')
    print()

  