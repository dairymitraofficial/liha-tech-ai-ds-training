l = [1, [2, [3, 4], 5], 6]

for i in l:
    if isinstance(i, list):
        print("LIST")
    else:
        print("NUMBER")