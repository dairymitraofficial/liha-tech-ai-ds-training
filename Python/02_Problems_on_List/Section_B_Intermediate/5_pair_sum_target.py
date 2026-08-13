l = [2, 7, 11, 15]
target = 9

for i in l:
    for j in l:
        if i+j == target:
            print("Pair = (", i, j, ")")
            exit()