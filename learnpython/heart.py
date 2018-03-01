for row in range(0, 6):
    for col in range(0, 7):
        if (col % 3 != 0 and row == 0) or (col % 3 == 0 and row == 1) or (row - col == 2) or (row + col == 8):
            print("%", end=" ")
        else:
            print("", end="  ")

    print()