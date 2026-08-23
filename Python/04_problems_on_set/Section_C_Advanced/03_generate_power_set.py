s = {1, 2, 3}

power_set = {frozenset()}

for element in s:
    power_set |= {subset | {element} for subset in power_set}

print("Number of subsets =", len(power_set))
print("Subsets:")

for subset in power_set:
    print(set(subset))
