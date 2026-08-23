text = input("Enter a sentence: ")

words = text.lower().split()

frequency = {}

for word in words:

    if word in frequency:
        frequency[word] = frequency[word] + 1
    else:
        frequency[word] = 1

for word in frequency:
    print(word, ":", frequency[word])