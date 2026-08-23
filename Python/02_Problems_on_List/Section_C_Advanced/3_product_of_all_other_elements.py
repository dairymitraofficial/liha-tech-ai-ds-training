lst = [1, 2, 3, 4]

result = []

for i in range(len(lst)):

    product = 1

    for j in range(len(lst)):

        if i != j:
            product = product * lst[j]

    result.append(product)

print("Result =", result)