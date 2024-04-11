'''
Understand the problem:
    input- list
    output- sorted list based off sorting algorithm (same list. Not a new list object)
    explicit:
    -return same list
    -list contains at least two elements
    implicit:
    -can sort strings and ints

examples/test cases:

Data structure
    loop
    element reassignment

algorithm:

While True:
    switch = False

    loop through list
        if first element is less than second element
            continue
        first element, second element = second element, first element
        switch = True
    if not switch
        break

'''

def bubble_sort(list):
    while True:
        switch = False
        for idx in range(1, len(list)):
            if list[idx-1] <= list[idx]:
                continue
            list[idx -1], list[idx] = list[idx], list[idx -1]
            switch = True
        if not switch:
            break

lst1 = [5, 3]
bubble_sort(lst1)
print(lst1)    # [3, 5]

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2)    # [1, 2, 4, 6, 7]

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel', 'Kim', 'Bonnie']
bubble_sort(lst3)
print(lst3)    # ["Alice", "Bonnie", "Kim", "Pete", "Rachel", "Sue", "Tyler"]