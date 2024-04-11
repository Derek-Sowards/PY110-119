#Understand the problem
'''
input:list
output: list with running total. 
implicit: 
explicit: 
-returned list needs the same amout of elements
-each element of returned list need to be incremented by previous element
'''
#Examples/Test cases
"""
print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True
"""
#Data structures
"""
list
"""
#Algorithm
"""
set an empty list
loop through list and add each element with previous element added
return new list
"""
#Code

def running_total(lst):
    return_list = []
    for element in lst:
        if len(return_list) == 0:
            return_list.append(element)
        else:
            return_list.append(element + return_list[-1])
    return return_list


def running_total(input):
    for idx, element in enumerate(input):
        if idx != 0:
            input[idx] = (element + input[idx -1])
    return input

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True