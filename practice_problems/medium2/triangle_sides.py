'''
Understand the problem
input- three integers
output- string (type of triangle)
explicit:
Equilateral- All three sides have the same length.
Isosceles- Two sides have the same length, while the third is different.
Scalene- All three sides have different lengths
invalid - two shortest sides combined not greater than the longest side, or any side is 0

examples/test cases

Data structure:

algorithm:
sort the list in ascending order
if first element is 0 or first element + second element is less than or equal to the third element, 
    return 'invalid'
elif: first element = second element = third element 
    return 'equilateral'
elif: first element does not equal second element and second element does not equal third element
    return 'scalene
else:
    return 'isosceles'

'''
def triangle(side1, side2, side3):
    ordered_sides = [side1, side2, side3]
    ordered_sides.sort()

    if ordered_sides[0] == 0 or ordered_sides[0] + ordered_sides[1] <= ordered_sides[2]:
        return 'invalid'
    elif ordered_sides[0] == ordered_sides[1] == ordered_sides[2]:
        return 'equilateral'
    elif ordered_sides[0] != ordered_sides[1]  != ordered_sides[2]:
        return 'scalene'
    return 'isosceles'
    


print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True