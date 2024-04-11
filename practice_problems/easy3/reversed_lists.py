'''
Understand the Problem:
input - list
output - list reversed in place
explicit - have to mutate the list. .reverse()
implicit -

Examples/Test Cases

Data structure

Algorithm
'''
def reverse_list(list):
    left_index = 0
    right_index = len(list) - 1

    while left_index < len(list) // 2:
        list[left_index], list[right_index] = list[right_index], list[left_index]
        left_index += 1
        right_index -= 1
    return list

list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result)  # prints [4, 3, 2, 1]
print(list1 is result)  # prints True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list(list2)
print(result2)  # prints ['e', 'd', 'c', 'b', 'a']
print(list2 is result2)  # prints True

list3 = ["abc"]
result3 = reverse_list(list3)
print(result3)  # prints ['abc']
print(list3 is result3)  # prints True

list4 = []
result4 = reverse_list(list4)
print(result4)  # prints []
print(list4 is result4)  # prints True