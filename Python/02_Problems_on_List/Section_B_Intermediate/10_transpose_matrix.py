l = [[1, 2, 3],
     [4, 5, 6]]

l2 = []

for i in range(len(l[0])):
    row = []

    for j in range(len(l)):
        row.append(l[j][i])

    l2.append(row)

print(l2)