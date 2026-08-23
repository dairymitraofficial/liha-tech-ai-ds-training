S1 = "python is easy and powerful"
S2 = "python is popular and useful"
s = set()
s1 = S1.split()
s2 = S2.split()

for i in s1:
    if i in s2:
        s.add(i)

print(s)

