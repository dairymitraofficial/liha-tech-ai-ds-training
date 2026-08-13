l = [1, 2, 3, 4, 5, 6, 7, 8]
l2 = []
s = 4

for i in range(0, len(l), s):
    l2.append(l[i:i+s])

print(l2)