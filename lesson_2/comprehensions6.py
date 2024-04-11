lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

def increment_values(dct):
    return {key: value + 1 for key, value in dct.items()}

incremeneted = [increment_values(element)
    for element in lst
]
print(incremeneted)