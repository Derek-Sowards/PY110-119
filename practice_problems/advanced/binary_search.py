'''
Understand the Problem:
    input- (list, search_item)
    output- index of search item, else -1(not found)
    explicit:
    -use a binary search implementation
    implicit:
    list argument will always be sorted

Examples/test Cases
Data structure:

Algorithm:
function(list, find)
set first idx
set last idx

Retrieve the middle value from the data
If the middle value is equal to 'Smith', stop the search.
If the middle value is less than 'Smith':
Discard the lower half, including the middle value
Repeat the process from the top, using the upper half as the starting data.

'''
def binary_search(list, target):
    low = 0
    high = len(list) -1

    while low <= high:
        mid = (low + high) // 2
        mid_val = list[mid]
        if mid_val < target:
            low = mid + 1
        elif mid_val > target:
            high = mid -1   
        else:
            return mid
        
    return -1


# All of these examples should print True
businesses = ['Apple Store', 'Bags Galore', 'Bike Store',
              'Donuts R Us', 'Eat a Lot', 'Good Food',
              'Pasta Place', 'Pizzeria', 'Tiki Lounge',
              'Zooper']
print(binary_search(businesses, 'Pizzeria') == 7)
print(binary_search(businesses, 'Apple Store') == 0)

print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 77) == -1)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 89) == 6)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 5) == 1)

names = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue',
         'Tyler']
print(binary_search(names, 'Peter') == -1)
print(binary_search(names, 'Tyler') == 6)