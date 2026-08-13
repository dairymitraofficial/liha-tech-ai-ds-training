l = [-5, 3, -2, 7, 0, -1]
pos = []
neg = []
for i in l:
    if i != 0:
        if i < 0:
            neg.append(i)
        else:
            pos.append(i)
print("Positive = ", pos)
print("Negative = ", neg)