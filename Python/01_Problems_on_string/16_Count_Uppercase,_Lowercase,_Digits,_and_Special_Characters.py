text = input("Enter a string: ")

uppercase = 0
lowercase = 0
digits = 0
special = 0

for char in text:

    if char.isupper():
        uppercase = uppercase + 1

    elif char.islower():
        lowercase = lowercase + 1

    elif char.isdigit():
        digits = digits + 1

    else:
        special = special + 1

print("Uppercase =", uppercase)
print("Lowercase =", lowercase)
print("Digits =", digits)
print("Special =", special)