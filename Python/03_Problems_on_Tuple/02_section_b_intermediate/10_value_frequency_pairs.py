tup = (1, 1, 2, 3, 3, 3)

result = []

for i in tup:
    if i not in result:
        result.append(i)

answer = []

for i in result:
    answer.append((i, tup.count(i)))

print(tuple(answer))