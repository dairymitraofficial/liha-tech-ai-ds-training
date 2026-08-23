text = input("Enter a string: ")
substring = input("Enter substring: ")

positions = []

for i in range(len(text) - len(substring) + 1):

    if text[i:i + len(substring)] == substring:
        positions.append(i)

print("Positions =", positions)