words = ['abc', 'xyz', 'aba', '1221']

count = 0

for i in words:
    if len(i) >= 2 and i[0] == i[-1]:
        count+=1

print(count)