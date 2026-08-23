universe = {1, 2, 3, 4, 5}
sets = {
    "S1": {1, 2, 3},
    "S2": {2, 4},
    "S3": {3, 4, 5}
}

best_pair = None

names = list(sets)

for i in range(len(names)):
    for j in range(i + 1, len(names)):
        pair = (names[i], names[j])
        if sets[pair[0]] | sets[pair[1]] == universe:
            best_pair = pair
            break
    if best_pair:
        break

print("Smallest covering pair =", best_pair)
