n = int(input("Enter a number: "))

last = n % 10

temp = n

count = 0

while temp >= 10:
    temp = temp // 10
    count = count + 1

first = temp

middle = n % (10 ** count)
middle = middle // 10

new_number = last * (10 ** count) + middle * 10 + first

print("After swapping =", new_number)