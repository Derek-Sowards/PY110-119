'''
understand the problem:
input- 3 integers (angles of triangle)
output- string (acute, invalid, right, obtuse)
explicit:
Right: One angle is a right angle (exactly 90 degrees).
Acute: All three angles are less than 90 degrees.
Obtuse: One angle is greater than 90 degrees.
invalid: sum of angles not 180, any angle is 0

implicit:

examples/test cases

Data structure
    list

algorithm:
    turn integers into a list and sort the lsit
    if first element lst == 0 or sum of list != 180
        return invalid
    elif last element < 90
        return acute
    elif 90 in list
        return right
    return obtuse
'''
def triangle(ang1, ang2, ang3):
    sorted_ang = [ang1, ang2, ang3]
    sorted_ang.sort()

    if sorted_ang[0] == 0 or sum(sorted_ang) != 180:
        return 'invalid'
    elif sorted_ang[2] < 90:
        return 'acute'
    elif 90 in sorted_ang:
        return 'right'
    return 'obtuse'


print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True