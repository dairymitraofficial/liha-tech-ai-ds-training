lst = [100, 4, 200, 1, 3, 2]

lst.sort()

longest = []
current = []

for i in range(len(lst)):

    if i == 0:
        current.append(lst[i])

    elif lst[i] == lst[i - 1] + 1:
        current.append(lst[i])

    else:
        if len(current) > len(longest):
            longest = current

        current = [lst[i]]

if len(current) > len(longest):
    longest = current

print("Sequence =", longest)
print("Length =", len(longest))