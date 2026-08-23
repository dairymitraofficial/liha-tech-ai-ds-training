text = input("Enter encoded string: ")

result = ""
i = 0

while i < len(text):

    char = text[i]
    i = i + 1

    number = ""

    while i < len(text) and text[i].isdigit():
        number = number + text[i]
        i = i + 1

    result = result + char * int(number)

print("Decoded string =", result)