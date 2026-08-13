# l =  [1, 2, 3, 4, 5, 7, 8, 9]

# for i in range(len(l)):
#     if (i+1) != l[i]:
#         print("Missing number = ", i+1)
#         exit()

l = [1, 2, 4, 5, 6]
n = 6

expected_sum = n * (n + 1) // 2
actual_sum = sum(l)

missing = expected_sum - actual_sum

print("Missing number =", missing)