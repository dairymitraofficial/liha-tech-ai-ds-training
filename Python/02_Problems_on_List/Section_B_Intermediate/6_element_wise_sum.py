l1 = [1, 2, 3]
l2 = [4, 5, 6]

l3 = [] 

for i in range(max(len(l1), len(l2))):
    add = l1[i] + l2[i]
    l3.append(add)

print(l3)