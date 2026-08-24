data = (
    ('Amit', 'DS'),
    ('Neha', 'AI'),
    ('Ravi', 'DS')
)

ds = []
ai = []

for i in data:
    if i[1] == 'DS':
        ds.append(i[0])

    elif i[1] == 'AI':
        ai.append(i[0])

print("DS =", tuple(ds))
print("AI =", tuple(ai))