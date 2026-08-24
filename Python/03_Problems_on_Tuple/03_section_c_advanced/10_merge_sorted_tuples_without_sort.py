tup1 = (1, 4, 7)
tup2 = (2, 3, 8, 9)

result = []

i = 0
j = 0

while i < len(tup1) and j < len(tup2):

    if tup1[i] < tup2[j]:
        result.append(tup1[i])
        i += 1

    else:
        result.append(tup2[j])
        j += 1

while i < len(tup1):
    result.append(tup1[i])
    i += 1

while j < len(tup2):
    result.append(tup2[j])
    j += 1

print(tuple(result))