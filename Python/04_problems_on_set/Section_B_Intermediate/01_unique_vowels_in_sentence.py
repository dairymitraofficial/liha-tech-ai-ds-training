sentence = "Education is a powerful tool"

vowels = set("aeiou")
found = set(sentence.lower()) & vowels

print("Vowels =", found)
