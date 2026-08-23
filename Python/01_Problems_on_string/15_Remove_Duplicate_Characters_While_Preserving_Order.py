text = input("Enter a string: ")

result = ""

for char in text:
    if char not in result:
        result = result + char

print("Unique characters =", result)