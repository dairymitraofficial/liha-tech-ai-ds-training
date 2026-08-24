students = (
    (101, 'Amit', 85),
    (102, 'Neha', 92),
    (103, 'Ravi', 85)
)

result = sorted(students, key=lambda x: (x[2], x[1]))

print(tuple(result))