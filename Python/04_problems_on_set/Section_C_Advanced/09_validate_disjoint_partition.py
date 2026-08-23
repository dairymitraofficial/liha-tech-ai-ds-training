universe = {1, 2, 3, 4, 5}
groups = [{1, 2}, {3, 4}, {5}]

union = set().union(*groups)
disjoint = all(groups[i].isdisjoint(groups[j])
               for i in range(len(groups))
               for j in range(i + 1, len(groups)))

valid = union == universe and disjoint

print("Valid disjoint partition =", valid)
