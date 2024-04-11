# def string_to_signed_integer(string):
#     value_dict = {
#         '0': 0,
#         '1': 1,
#         '2': 2,
#         '3': 3,
#         '4': 4,
#         '5': 5,
#         '6': 6,
#         '7': 7,
#         '8': 8,
#         '9': 9,
#     }
#     if string[0] in ['+', '-']:
#         operator = string[0]
#         if operator == '-':
#             value = 0
#             for char in string[1:]:
#                 value = (value * 10) + value_dict[char]
#             return value * -1
#         else:
#             value = 0
#             for char in string[1:]:
#                 value = (value * 10) + value_dict[char]
#             return value 
#     return positive_string_value(string, value_dict)

# def positive_string_value(string, value_dict):
#     value = 0
#     for char in string:
#         value = (value * 10) + value_dict[char]
#     return value

def string_to_integer(string):
    numbers_dict = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
    }
    value = 0
    for char in string:
        value = (10 * value) + numbers_dict[char]
    return value

def string_to_signed_integer(string):
    match string[0]:
        case '-':
            return -string_to_integer(string[1:])
        case '+':
            return string_to_integer(string[1:])
        case _:
            return string_to_integer(string)


print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True