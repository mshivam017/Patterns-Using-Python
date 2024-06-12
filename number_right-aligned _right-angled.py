row = int(input("Enter Number of Rows: "))
col= row
for i in range(1,row+1):
    num= (row+1)-i
    for j in range(1,col+1):
        if j<=(row+1)-i:
            print(num , end='')
            num = num-1
        else:
            print(' ', end='')
    print()