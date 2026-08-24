tup = (1, 2, 2, 3, 1, 4)
lst = []

for i in tup:
    if i not in lst:
        lst.append(i)
print(tuple(lst))