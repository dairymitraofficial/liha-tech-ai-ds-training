text = input("Enter string: ")
pattern = input("Enter pattern: ")

minimum = ""

for i in range(len(text)):

    current = ""

    for j in range(i, len(text)):

        current = current + text[j]

        found = True

        for char in pattern:

            if current.count(char) < pattern.count(char):
                found = False
                break

        if found:

            if minimum == "" or len(current) < len(minimum):
                minimum = current

            break

print("Minimum window =", minimum)