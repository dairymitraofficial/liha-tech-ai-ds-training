l = [1, 2, 2, 3, 1, 4]

l2 = []

for i in l:
    if i not in l2:
        l2.append(i)
    
print(l2)