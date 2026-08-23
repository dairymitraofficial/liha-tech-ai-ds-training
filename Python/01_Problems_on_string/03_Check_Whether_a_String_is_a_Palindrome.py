text = input("Enter a string: ")

reverse = ""

for char in text:
    reverse = char + reverse

if text == reverse:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")