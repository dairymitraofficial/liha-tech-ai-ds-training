tup1 = (1, 2)
tup2 = ('A', 'B')

result = []

for i in tup1:
    for j in tup2:
        result.append((i, j))

print(tuple(result))