lst = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

result = []

for i in range(len(lst) - k + 1):

    window = lst[i:i + k]

    maximum = window[0]

    for num in window:
        if num > maximum:
            maximum = num

    result.append(maximum)

print("Maximum values =", result)