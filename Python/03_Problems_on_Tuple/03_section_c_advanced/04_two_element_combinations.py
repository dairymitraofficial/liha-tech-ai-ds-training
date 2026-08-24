tup = (1, 2, 3, 4)

result = []

for i in range(len(tup)):
    for j in range(i + 1, len(tup)):
        result.append((tup[i], tup[j]))

print(tuple(result))