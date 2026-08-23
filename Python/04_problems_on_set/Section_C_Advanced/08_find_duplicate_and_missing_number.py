numbers = [1, 2, 2, 4, 5]
n = 5

expected = set(range(1, n + 1))
actual = set(numbers)

duplicate = set()

for num in numbers:
    if numbers.count(num) > 1:
        duplicate.add(num)

missing = expected - actual

print("Duplicate =", duplicate.pop())
print("Missing =", missing.pop())