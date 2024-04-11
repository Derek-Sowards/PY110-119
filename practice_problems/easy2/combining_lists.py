'''
Understand the Problem
    input- two lists [1, 2, 3, 4] [1, 3, 4, 5]
    output- one set that contains values from both lists {1, 2, 3, 4, 5}
    explicit- assume that the arguments will always be lists
    
Algorithm
    transform both lists into sets and use the union operator'''

def union(lst1, lst2):
    return set(lst1) | set(lst2)

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True