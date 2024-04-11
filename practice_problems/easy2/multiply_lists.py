def multiply_list(list1, list2):
    for idx in range(len(list1)):
        list1[idx] *= list2[idx]
    return list1


list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True