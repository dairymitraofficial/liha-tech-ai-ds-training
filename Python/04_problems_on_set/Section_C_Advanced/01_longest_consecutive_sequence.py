numbers = {100, 4, 200, 1, 3, 2}

longest = []

for num in numbers:
    if num - 1 not in numbers:
        current = num
        sequence = []

        while current in numbers:
            sequence.append(current)
            current += 1

        if len(sequence) > len(longest):
            longest = sequence

print("Sequence =", longest)
print("Length =", len(longest))