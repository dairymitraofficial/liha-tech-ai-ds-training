l =[10, 20, 30, 40]
print("Your list is- ", l)
search = int(input("Enter elemet to search- "))

found = False

for i in range(len(l)):
    if l[i]==search:
        print(search, " found at index ", i)
        found = True

if found == False:
    print(search, "not found")
