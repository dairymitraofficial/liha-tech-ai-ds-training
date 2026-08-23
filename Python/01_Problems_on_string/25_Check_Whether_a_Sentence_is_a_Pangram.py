text = input("Enter a sentence: ")

text = text.lower()

alphabet = "abcdefghijklmnopqrstuvwxyz"

pangram = True

for char in alphabet:

    if char not in text:
        pangram = False
        break

print("Pangram =", pangram)