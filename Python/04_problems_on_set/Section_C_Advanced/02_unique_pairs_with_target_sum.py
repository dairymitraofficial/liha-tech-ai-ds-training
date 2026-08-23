numbers = [2, 7, 11, 15, 1, 8]
target = 9

seen = set()
pairs = set()

for num in numbers:
    complement = target - num

    if complement in seen:
        pairs.add(tuple(sorted((num, complement))))

    seen.add(num)

print("Pairs =", pairs)