tup = (1, 2, 2, 3, 4, 4, 4)

repeated = []

for i in tup:
    if tup.count(i) > 1 and i not in repeated:
        repeated.append(i)

print("Repeated values =", tuple(repeated))