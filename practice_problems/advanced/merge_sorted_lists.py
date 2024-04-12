'''
Understand the problem:
input- 2 lists
output- 1 list containing all elements from both lists in ascending order
explicit:
    can not use a solution where you sort the result list. 
    You must build the list 1 element at a time
    dont mutate the input lists.

examples/test cases:
Data structure:
'''

def merge(list1, list2):
    result = []
    copy1 = list1[:]
    copy2 = list2[:]

    while copy1 and copy2:
        if copy1[0] < copy2[0]:
            result.append(copy1.pop(0))
        else:
            result.append(copy2.pop(0))

    return result + (copy1 if not copy2 else copy2)    
    
        

print(merge([1, 5, 9], [2, 6, 8]))      # [1, 2, 5, 6, 8, 9]
print(merge([1, 1, 3], [2, 2]))         # [1, 1, 2, 2, 3]
print(merge([], [1, 4, 5]))             # [1, 4, 5]
print(merge([1, 4, 5], []))             # [1, 4, 5]