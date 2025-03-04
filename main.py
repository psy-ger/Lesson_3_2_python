first_list = [1, 2, 3, 4, 5, 6, 3]

if not first_list or len(first_list) == 1:
    print(first_list)
else:
    variable_end = first_list[-1]
    result_list = first_list.pop()
    first_list.insert(0, variable_end)
    print(first_list)
