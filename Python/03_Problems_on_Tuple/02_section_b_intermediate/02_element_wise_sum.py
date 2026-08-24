tup1 = (1, 2, 3)
tup2 = (4, 5, 6)

lst = []
for i in range(len(tup1)):
    total = tup1[i] + tup2[i]
    lst.append(total)
print(tuple(lst))