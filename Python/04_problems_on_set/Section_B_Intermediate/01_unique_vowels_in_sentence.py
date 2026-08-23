s = "Education is a powerful tool"

s = set(s)
vovels = set()
for i in s:
    if i in "aeiouAEIOU":
        vovels.add(i)

print(vovels)
