s = {1, 2, 3}

power_set = {frozenset()}

for element in s:
    new_subsets = set()

    for subset in power_set:
        new_subsets.add(subset | frozenset({element}))

    power_set.update(new_subsets)

print("Number of subsets =", len(power_set))

for subset in power_set:
    print(set(subset))