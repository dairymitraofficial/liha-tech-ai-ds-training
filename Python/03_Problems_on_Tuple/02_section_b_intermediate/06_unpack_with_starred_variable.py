tup = ((1, 'A'), (2, 'B'), (3, 'C'))

numbers = []
letters = []

for i in tup:
    numbers.append(i[0])
    letters.append(i[1])

print("Numbers =", tuple(numbers))
print("Letters =", tuple(letters))