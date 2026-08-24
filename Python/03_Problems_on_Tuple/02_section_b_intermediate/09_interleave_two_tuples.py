tup1 = (1, 3, 5)
tup2 = (2, 4, 6)

result = []

for i in range(len(tup1)):
    result.append(tup1[i])
    result.append(tup2[i])

print(tuple(result))