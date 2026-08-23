words = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
rem_index  = [0, 4, 5]
new_list = []
for i in range(len(words)):
    if i not in rem_index:
        new_list.append(words[i])

print(new_list)