str = input("Enter a string- ")

str2 = ""

for i in str:
    if i not in str2:
        str2 = str2 + i

print(str2)