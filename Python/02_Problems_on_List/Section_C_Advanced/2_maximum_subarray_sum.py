lst = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

max_sum = lst[0]
current_sum = 0

start = 0
best_start = 0
best_end = 0

for i in range(len(lst)):
    current_sum = current_sum + lst[i]

    if current_sum > max_sum:
        max_sum = current_sum
        best_start = start
        best_end = i

    if current_sum < 0:
        current_sum = 0
        start = i + 1

subarray = lst[best_start:best_end + 1]

print("Maximum sum =", max_sum)
print("Subarray =", subarray)