words = ['apple', 'cat', 'banana', 'dog', 'elephant']
n = 5
new_l = []
for i in words:
    if len(i) > n:
        new_l.append(i)
print(new_l)
