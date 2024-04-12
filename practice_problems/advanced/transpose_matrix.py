'''
Understand the problem:
    input - list of lists (each sub list has three items)
    output - transposed matrix. (each element in corresponding idx in same list)
    explicit:
    -no modifying the original matrix (return new nested list)

Examples/test cases:

data structure:
    for loops
    new list

algorithm:
    create result list 
    iterate through lists:
        create empty list
        take idx element and append it to empty list
        add empty list to result list
    return result list

'''
def transpose(matrix):
    result_list = [[],[],[]]
    for sublist in matrix:
        for idx in range(0, len(sublist)):
            result_list[idx].append(sublist[idx])
    return result_list




matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

new_matrix = transpose(matrix)

print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True