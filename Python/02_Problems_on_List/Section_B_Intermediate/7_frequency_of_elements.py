l = [1, 2, 2, 3, 3, 3, 2, 1]

counted = []

for i in l:
    if i not in counted:
        count = 0

        for j in l:
            if i == j:
                count += 1

        print(i, "->", count)
        counted.append(i)