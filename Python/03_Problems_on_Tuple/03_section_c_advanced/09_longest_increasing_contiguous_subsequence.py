tup = (1, 2, 5, 3, 4, 6, 7, 2)

current = [tup[0]]
longest = [tup[0]]

for i in range(1, len(tup)):

    if tup[i] > tup[i - 1]:
        current.append(tup[i])

    else:
        if len(current) > len(longest):
            longest = current

        current = [tup[i]]

if len(current) > len(longest):
    longest = current

print("Subsequence =", tuple(longest))
print("Length =", len(longest))