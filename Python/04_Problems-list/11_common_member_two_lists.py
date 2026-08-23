def common_member(list1, list2):
    common_el = False

    for i in list1:
        if i in list2:
            common_el = True

    return common_el


list1 = [1, 2, 3, 4, 5]
list2 = [8, 9, 3, 10, 11]

print(common_member(list1, list2))