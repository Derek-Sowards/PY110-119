def rotate90(matrix):
    rotated_matrix = []
    for _ in matrix[0]:
        rotated_matrix.append([])
    
    for sublist in matrix:
        for idx in range(0, len(sublist)):
            rotated_matrix[idx].insert(0, sublist[idx])
    return rotated_matrix




matrix1 = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

matrix2 = [
    [3, 7, 4, 2],
    [5, 1, 0, 8],
]

new_matrix1 = rotate90(matrix1)
new_matrix2 = rotate90(matrix2)
new_matrix3 = rotate90(rotate90(rotate90(rotate90(matrix2))))

# These examples should all print True
print(new_matrix1 == [[3, 4, 1], [9, 7, 5], [6, 2, 8]])
print(new_matrix2 == [[5, 3], [1, 7], [0, 4], [8, 2]])
print(new_matrix3 == matrix2)