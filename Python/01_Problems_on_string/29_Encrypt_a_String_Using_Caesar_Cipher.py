text = input("Enter text: ")
shift = int(input("Enter shift: "))

result = ""

for char in text:

    if char.isalpha():

        if char.isupper():
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

        else:
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

        result = result + new_char

    else:
        result = result + char

print("Encrypted text =", result)