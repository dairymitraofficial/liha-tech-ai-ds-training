text1 = input("Enter first string: ")
text2 = input("Enter second string: ")

text1 = text1.replace(" ", "").lower()
text2 = text2.replace(" ", "").lower()

if text1 == text2:
    print("Strings are equal after normalization = True")
else:
    print("Strings are equal after normalization = False")