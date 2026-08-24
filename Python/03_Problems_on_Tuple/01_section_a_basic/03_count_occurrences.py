tup = (1, 2, 2, 3, 2, 4)
element = 2

count = 0

for i in tup:
    if element == i:
        count += 1

print("Occurrences of ", element, " = ", count )