numbers = [1, 2, 3, 2, 4, 1, 5, 3]

l = []

for i in numbers:
    if i not in l:
        l.append(i)
print(l)