'''
understand the Problem
    input - string of digits '4321'
    output - string as a number 4321
    explicit - do not use the built in function int(), dont worry about invalid characters
    questions Q: what if the string is empty? Leading or trailing whitespace?

Examples / test cases

Data structure
    conversion dictionary (keys = string values = integers)

Algorithm
    create a conversion dictionary for 0-9
    return_value = 0

    iterate through every char in input string
        convert char to int and add that to return value * by 10
    
    return the return_value
'''
def string_to_integer(string):
    conversion_dictionary = {
        '0' : 0,
        '1' : 1,
        '2' : 2,
        '3' : 3,
        '4' : 4,
        '5' : 5,
        '6' : 6,
        '7' : 7,
        '8' : 8,
        '9' : 9,
    }
    return_value = 0

    for char in string:
        return_value  = (return_value * 10) + conversion_dictionary[char]
    return return_value

def string_to_signed_integer(string):
    match string[0]:
        case '+':
            return string_to_integer(string[1:])
        case '-':
            return -string_to_integer(string[1:])
        case _:
            return string_to_integer(string)


print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True