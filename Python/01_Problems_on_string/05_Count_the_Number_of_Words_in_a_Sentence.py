text = input("Enter a sentence: ")

words = text.split()

count = 0

for word in words:
    count = count + 1

print("Word count =", count)