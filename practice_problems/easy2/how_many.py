'''
Understand the problem
input-list
output- print each element and their # of occurences

Examples/Test Cases
vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)

# your output sequence may appear in a different sequence
car => 4
truck => 3
SUV => 1
motorcycle => 2

Data structure
dictionary

Algorithm

Create an empty dictionary
iterate through list add each new element to list, and if element is not present, add the key
iterate through dictionary items and print key, value
'''
def count_occurrences(list):
    counted = {}
    for element in list:
        counted[element.casefold()] = counted.get(element.casefold(), 0) + 1
    
    for key, value in counted.items():
        print(f'{key} => {value}')


vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'suv', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)
