text = input("Enter a string: ")

digits = ""

for char in text:
    if char.isdigit():
        digits = digits + char

print("Digits =", digits)