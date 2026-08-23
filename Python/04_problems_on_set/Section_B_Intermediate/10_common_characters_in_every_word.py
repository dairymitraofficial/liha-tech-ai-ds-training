words = ['bella', 'label', 'roller']

common = set(words[0])

for word in words[1:]:
    common = common.intersection(set(word))

print("Common characters =", common)