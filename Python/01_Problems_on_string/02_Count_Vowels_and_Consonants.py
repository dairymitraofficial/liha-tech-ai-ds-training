text = input("Enter a string: ")

vowels = 0
consonants = 0

for char in text:
    if char.isalpha():
        if char.lower() in "aeiou":
            vowels = vowels + 1
        else:
            consonants = consonants + 1

print("Vowels =", vowels)
print("Consonants =", consonants)