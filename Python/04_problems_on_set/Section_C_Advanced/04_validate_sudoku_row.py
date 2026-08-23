row = [5, 3, 4, 6, 7, 8, 9, 1, 2]

valid = len(row) == 9 and set(row) == set(range(1, 10))

print("Valid Sudoku row =", valid)
