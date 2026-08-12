str = input("Enter a str = ")
upper = 0
lower = 0
num = 0
special = 0


for i in str:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower+=1
    elif i.isnumeric():
        num += 1
    else:
        special += 1

print(upper)
print(lower)
print(num)
print(special)