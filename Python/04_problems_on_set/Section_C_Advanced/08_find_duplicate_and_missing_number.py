numbers = [1, 2, 2, 4, 5]
n = 5

expected = set(range(1, n + 1))
actual = set(numbers)

duplicate = next(num for num in numbers if numbers.count(num) > 1)
missing = (expected - actual).pop()

print("Duplicate =", duplicate)
print("Missing =", missing)
