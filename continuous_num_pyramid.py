row = int(input("Enter Number Of Rows: "))
col= row
num = 1
for i in range(1,row+1):
    for j in range(1,col+1):
        if j<=i:
            print(num, end='')
            num=num+1
        else:
            print(' ', end='')
    print()