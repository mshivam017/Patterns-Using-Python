row = int(input("Enter Number Of Rows: "))
col= row
for i in range(1,row+1):
    for j in range(1,col+1):
        if j<=i:
            print(i, end='')
        else:
            print(' ', end='')
    print()