first_list = [1, 2, 3, 4, 5, 6, 2]

if not first_list or len(first_list) == 1:
    print(first_list)
else:
    result_list = first_list.pop()
    first_list.insert(0, result_list)
    print(first_list)
