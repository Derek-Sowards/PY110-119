'''
Understand the problem
input- integer
output- integer with max rotations performed
explicit:
after each rotation, lock the digit that was just rotated and rotate the rest of the integer
735291
352917 = 3 52917 then rotate 1st number to the end (5)
329175 = 32 9175 then rotate 1st number to the end (9)
321759 = 321 759 then rotate 1st number to the end (7)
321597 = 3215 97 then rotate 1st number to the end (9)
321579

examples/test cases:

data structure
str()
for loop
rotation function

algorithm:
turn number into string
initialize an emtpy string
loop through string
    rotate string
    pop off first string character to empty string
turn empty string into integer
return integer

'''
def max_rotation(number):
    number_str = str(number)
    rotated = ''
    while number_str:
        result = rotate_string(number_str)
        rotated += result[0]
        number_str = result[1:]
    return int(rotated)

def rotate_string(str):
    return str[1:] + str[0]


print(max_rotation(735291))         # 321579
print(max_rotation(3))              # 3
print(max_rotation(35))             # 53
print(max_rotation(105))            # 15 (the leading zero gets dropped)
print(max_rotation(8703529146))     # 7321609845