def multiply_elements(list1, list2):
    # return [list1[idx] * list2[idx] for idx in range(len(list1))]
    return [a * b for a, b in zip(list1, list2)]


print(multiply_elements([1, 2, 3], [4, 5, 6]))
# [4, 10, 18]