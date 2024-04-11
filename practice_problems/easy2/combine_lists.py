def interleave(lst1, lst2):
    list_of_tuples = list(zip(lst1, lst2))
    return [element for tup in list_of_tuples for element in tup]



list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True