universe = {1, 2, 3, 4, 5}

sets = {
    "S1": {1, 2, 3},
    "S2": {2, 4},
    "S3": {3, 4, 5}
}

names = list(sets.keys())
smallest_pair = None

for i in range(len(names)):
    for j in range(i + 1, len(names)):

        set1 = sets[names[i]]
        set2 = sets[names[j]]

        if set1.union(set2) == universe:
            smallest_pair = (names[i], names[j])
            break

    if smallest_pair:
        break

print("Smallest covering pair =", smallest_pair)