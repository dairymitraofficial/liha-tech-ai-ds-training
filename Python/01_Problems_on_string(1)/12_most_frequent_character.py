str = input("Enter a string: ")

frequency = {}

for i in str:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

most_frequent = max(frequency, key=frequency.get)

print("Most frequent character - ", most_frequent)