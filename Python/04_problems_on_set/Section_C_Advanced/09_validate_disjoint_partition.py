universe = {1, 2, 3, 4, 5}
groups = [{1, 2}, {3, 4}, {5}]

combined = set()

for group in groups:
    combined.update(group)

disjoint = True

for i in range(len(groups)):
    for j in range(i + 1, len(groups)):
        if not groups[i].isdisjoint(groups[j]):
            disjoint = False

valid = combined == universe and disjoint

print("Valid disjoint partition =", valid)