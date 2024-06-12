row=  int(input("Enter Number of Rows:  "))
col = row
for i in range(1,row+1):
    for j in range(1,col+1):
        num =j
        if j<=i:
            print(num, end='')
            num=num+1
        else:
            print(' ', end='')
    print()