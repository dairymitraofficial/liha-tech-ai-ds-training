words = ['bella', 'label', 'roller']

common = set(words[0])

for word in words[1:]:
    common &= set(word)

print("Common characters =", common)
