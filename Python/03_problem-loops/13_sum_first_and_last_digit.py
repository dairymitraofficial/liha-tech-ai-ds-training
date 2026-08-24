n = int(input("Enter a number: "))

last = n % 10

while n >= 10:
    n = n // 10

first = n

sum = first + last

print("Sum =", sum)