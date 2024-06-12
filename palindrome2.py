
for i in range(1,5):
    start_num = i
    for j in range(1,8):
        if j>=5-i and j<=3+i:
            print(start_num, end='')
            start_num += 1
            
        else:
            print(' ', end='')
    print()