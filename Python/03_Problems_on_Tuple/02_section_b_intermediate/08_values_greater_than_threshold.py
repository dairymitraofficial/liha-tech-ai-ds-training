tup = (5, 12, 3, 18, 7)

threshold = 10

result = []

for i in tup:
    if i > threshold:
        result.append(i)

print(tuple(result))