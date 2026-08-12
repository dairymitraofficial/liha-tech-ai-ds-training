char = input("Enter a Alphabate- ")
char = char.lower()

if char.isalpha():
    if char in "aeiou":
        print(char, "is a Vowel")

    else:
        print(char, "is a Consonant")

else:
    print("Please Enter a Alphabate!")