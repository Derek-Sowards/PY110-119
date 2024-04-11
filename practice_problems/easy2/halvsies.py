'''
Understand the Problem
    input- list of elements [1, 2, 3, 4]
    output- list containing two list elements from input list [[1, 2],[3, 4]]
    explicit - if original list contains odd number of elements, place middle element 
                with first list
    implicit-
    questions- Q: Will the inputs always be numbers?

Examples/ Test Cases
-if input list only contains 1 element, return list should be 2 lists, the 2nd being empty
-if input list is empty, return 2 empty list elements inside list.

Data structure
-lists
-element reference

Algorithm
    create an empty list element with 2 empty nested lists inside
    if length of list is odd
        add everything in input list from start to length of list / 2 + 1
    else:
        add everythin in input list from start to length of list / 2
    return new list

'''
# def halvsies(list):
#     nested_list = [[],[]]
#     list_length = len(list)
#     if list_length % 2 != 0:
#         nested_list[0]= (list[:(list_length // 2) + 1])
#         nested_list[1]= (list[(list_length // 2) + 1:])
#     else:
#         nested_list[0]= (list[: (list_length // 2)])
#         nested_list[1]= (list[(list_length // 2) : ])
#     return nested_list

def halvsies(lst):
    half = (len(lst)+1) // 2
    first_half = lst[:half]
    second_half = lst[half:]
    return [first_half, second_half]

# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])