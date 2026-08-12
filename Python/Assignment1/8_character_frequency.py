str = input("Enter a string- ")

frequency = {}

for i in str:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

print(frequency)