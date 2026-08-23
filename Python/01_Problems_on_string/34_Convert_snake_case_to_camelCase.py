text = input("Enter snake_case string: ")

words = text.split("_")

result = words[0]

for word in words[1:]:
    result = result + word.capitalize()

print("camelCase =", result)