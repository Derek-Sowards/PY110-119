'''
Understand the problem
input- list of integers
output- integer average rounded down to an integer
explicit- list will never be empty, numbers will always be positive
implicit- if list contains 1 integer, the avg will be that number

examples/test cases

data structure

algorithm
    set divisor by length of list
    find sum of the list
    return sum divided by len(list) rounded down to nearest integer
'''
def average(list):
    return sum(list) // len(list)

print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True