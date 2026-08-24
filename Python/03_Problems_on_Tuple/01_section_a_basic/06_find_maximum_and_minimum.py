tup = (8, 3, 15, 1, 9)


print("Maximum = ", max(tup))
print("Minimum = ", min(tup))
max_num = tup[0]
min_num = tup[0]

for i in tup:
    if i>max_num:
        max_num = i

    if i<min_num:
        min_num = i

print("Maximum = ", max_num)
print("Minimum = ", min_num)