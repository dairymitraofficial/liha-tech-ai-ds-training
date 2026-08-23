text = input("Enter a string: ")

pattern = ""
found = False

for i in range(1, len(text)):

    if len(text) % i == 0:

        pattern = text[:i]

        repeat_count = len(text) // i

        if pattern * repeat_count == text:

            if repeat_count > 1:
                found = True
                break

if found:
    print("Repeated pattern =", pattern)
    print("Repeat count =", repeat_count)
else:
    print("No repeated pattern found.")