lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
sorted_as_string = [sorted(sublist, key=str)
    for sublist in lst
]
print(sorted_as_string)