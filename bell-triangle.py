row = int(input('Enter No of Rows: '))
l1 = [1]
l2 = []

for i in range(1,1+row):
    l2.append(l1[-1])
    for e in l1:
        l2.append(e+l2[-1])
    print(l1)
    l1 = list(l2)
    l2.clear()