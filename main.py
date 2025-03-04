first_list = [1, 2, 3, 4, 5, 6, 8]

if not first_list or len(first_list) == 1:
    print(first_list)
else:
    first_list.insert(0, first_list.pop())
    print(first_list)
