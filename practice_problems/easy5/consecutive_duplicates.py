def unique_sequence(input_list):
    # return list(set(input_list))
    return [element for idx, element in enumerate(input_list)
             if idx == 0 or element != input_list[idx -1]]


print(unique_sequence([1, 1, 2, 3, 3, 3, 4, 5, 5, 6]))
# [1, 2, 3, 4, 5, 6]