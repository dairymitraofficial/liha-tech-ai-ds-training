text = input("Enter expression: ")

stack = []

for char in text:

    if char in "([{":
        stack.append(char)

    elif char in ")]}":

        if len(stack) == 0:
            print("Balanced = False")
            break

        last = stack.pop()

        if char == ")" and last != "(":
            print("Balanced = False")
            break

        if char == "]" and last != "[":
            print("Balanced = False")
            break

        if char == "}" and last != "{":
            print("Balanced = False")
            break

else:

    if len(stack) == 0:
        print("Balanced = True")
    else:
        print("Balanced = False")