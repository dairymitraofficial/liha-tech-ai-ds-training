s = {1, 2, 4, 5, 7, 10}
n = 10

s2 = set()
missing = set()
for i in range(n):
    s2.add(i+1)

for i in s2:
    if i not in s:
        missing.add(i)

print(missing)