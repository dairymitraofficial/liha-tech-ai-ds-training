str = input("Enter a string- ")
char = input("Enter a character- ")

first = str.find(char)
last = str.rfind(char)

print("First occurrence - ", first)
print("Last occurrence - ", last)