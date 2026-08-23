sentence = "python is easy and python is powerful"

seen = set()
duplicates = set()

words = sentence.split()

for word in words:
    if word in seen:
        duplicates.add(word)
    else:
        seen.add(word)

print("Duplicate words =", duplicates)