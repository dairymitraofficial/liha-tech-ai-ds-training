text = input("Enter a string: ")

result = ""

for char in text:

    if char.isalnum() or char == " ":
        result = result + char

print("Result =", result)