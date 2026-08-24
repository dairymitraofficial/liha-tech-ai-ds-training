matrix = ((1, 2, 3),
          (4, 5, 6))

result = []

for i in range(3):
    row = []

    for j in range(2):
        row.append(matrix[j][i])

    result.append(tuple(row))

print(tuple(result))