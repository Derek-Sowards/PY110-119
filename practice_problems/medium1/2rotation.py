'''
understand the problem
input- original number, last 'count' digits to rotate (37482, 4)
output- rotated number. ----> (34827)
explicit rules- 
rotate the last count digits of the original number
leave the first digits in the same order

Examples/Test cases

Data structure
2 functions

Algorithm:
turn number into list
split original number list into two parts. 1- part that wont change 2- part that will change
pass the part that will change into helper function that will rotate the first number to last
return rotated number and append it to the end of part 1
turn back into string
'''
# def rotate_rightmost_digits(number, count):
#     number_list = [int(digit) for digit in str(number)] #----[7, 3, 4, 2, 9, 1]
#     first_half = number_list[:-count] # ---- [7, 3, 4, 2]
#     second_half = number_list[-count:] # ----- [9, 1]

#     rotated_list = first_half + rotate_list(second_half)
#     return int(''.join([str(num) for num in rotated_list]))
    

# def rotate_list(input_list):
#     return input_list[1:] + input_list[:1]

def rotate_rightmost_digits(number, count):
    number_str = str(number)
    first_half = number_str[:-count]
    second_half = number_str[-count:]
    result_string = first_half + rotate_string(second_half)

    return int(result_string)

def rotate_string(str):
    return str[1:] + str[0]







print(rotate_rightmost_digits(735291, 2))      # 735219
print(rotate_rightmost_digits(735291, 3))      # 735912
print(rotate_rightmost_digits(735291, 1))      # 735291
print(rotate_rightmost_digits(735291, 4))      # 732915
print(rotate_rightmost_digits(735291, 5))      # 752913
print(rotate_rightmost_digits(735291, 6))      # 352917