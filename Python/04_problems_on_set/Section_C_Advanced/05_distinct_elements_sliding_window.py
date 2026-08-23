numbers = [1, 2, 1, 3, 4, 2, 3]
k = 4

counts = []

for i in range(len(numbers) - k + 1):
    window = numbers[i:i + k]
    counts.append(len(set(window)))

print("Distinct counts =", counts)
