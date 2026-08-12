char = input("Enter a Alphabate- ")

if char.isalpha():
    if char.isupper():
        print(char, "is a Uppercase Alphabet")
    else:
        print(char, "is a Lowercase  Alphabet")


else:
    print("Please Enter a Alphabate!")