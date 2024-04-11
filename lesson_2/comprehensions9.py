lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]
def are_they_even(element):
    return [item for item in element.values() if item % 2 == 0]
    

new_list = [element
    for element in lst
    if are_they_even(element)
]
print(new_list)