l1 = [1, 2, 3, 4, 5]
l2 = []
n = 3

for i in range(n):
    l2.append(l1[i])

for i in l2:
    l1.remove(i)

l1.extend(l2)

print(l1)
