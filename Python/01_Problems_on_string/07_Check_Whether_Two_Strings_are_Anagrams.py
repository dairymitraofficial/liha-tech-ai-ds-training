text1 = input("Enter first string: ")
text2 = input("Enter second string: ")

text1 = text1.lower()
text2 = text2.lower()

if sorted(text1) == sorted(text2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")