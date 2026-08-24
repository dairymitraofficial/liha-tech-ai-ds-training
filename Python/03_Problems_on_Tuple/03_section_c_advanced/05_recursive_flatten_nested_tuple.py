tup = (1, (2, (3, 4)), 5)

result = []

def flatten(data):
    for i in data:
        if isinstance(i, tuple):
            flatten(i)
        else:
            result.append(i)

flatten(tup)

print(tuple(result))