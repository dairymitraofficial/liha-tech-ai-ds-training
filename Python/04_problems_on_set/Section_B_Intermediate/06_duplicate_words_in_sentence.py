sentence = "python is easy and python is powerful"

words = sentence.lower().split()
seen = set()
duplicates = set()

for word in words:
    if word in seen:
        duplicates.add(word)
    else:
        seen.add(word)

print("Duplicate words =", duplicates)
