rows = int(input("Enter number of rows: "))

for i in range(1, rows+1):
    # Print leading spaces
    for space in range(rows - i):
        print("  ", end="")
    
    # Initialize starting number
    start_num = i
    
    # Print numbers increasing up to the middle of the row
    for j in range(i):
        print(start_num, end=" ")
        start_num += 1
    start_num -= 2
    
    # Print numbers decreasing after the middle of the row
    for j in range(i-1):
        print(start_num, end=" ")
        start_num -= 1
    
    # Move to the next line after each row
    print()
