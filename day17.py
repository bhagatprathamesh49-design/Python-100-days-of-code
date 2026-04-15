rows = int(input("Enter the number of rows: "))

for loop_1 in range(1, rows + 1):
    for loop_2 in range(1, loop_1 + 1):
        print(loop_2, end=" ")
    print()

for loop_1 in range(rows, 1, -1):
    for loop_2 in range(1, loop_1):
        print(loop_2, end=" ")
    print()
