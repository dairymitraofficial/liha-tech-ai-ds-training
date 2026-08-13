l = [1, 2, 3, 4, 5]
l2 = []
n= 2

for i in range(n):
    l2.append(l[i])

for i in l2:
    if i in l:
        l.remove(i)


print(l)
print(l2)

l.extend(l2)
print(l)