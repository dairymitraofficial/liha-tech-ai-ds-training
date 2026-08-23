lst = [1, 2, 3, 2, 1]
target = 5

result = []

for i in range(len(lst)):

    current_sum = 0

    for j in range(i, len(lst)):

        current_sum = current_sum + lst[j]

        if current_sum == target:
            result.append(lst[i:j + 1])

print("Subarrays =", result)