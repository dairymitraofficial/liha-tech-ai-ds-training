numbers = {1, 2, 4, 5, 7, 10}
n = 10

all_numbers = set(range(1, n + 1))
missing = all_numbers - numbers

print("Missing numbers =", missing)
