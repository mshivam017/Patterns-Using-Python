for i in range(1, 8):
    for j in range(1, 6):
        if ((j == 1 or j == 5) and (i != 1 and i!=4 and i != 7)) or ((i == 1 or i == 4 or i == 7) and (j >= 1 and j <= 4)) :
            print('*', end=' ')
        else:
            print(' ',end=' ')
    print()
