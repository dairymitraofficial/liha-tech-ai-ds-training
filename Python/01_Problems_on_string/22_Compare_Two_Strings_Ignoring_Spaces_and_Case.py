text = input("Enter a string: ")
n = int(input("Enter number of positions: "))

n = n % len(text)

result = text[n:] + text[:n]

print("Rotated string =", result)