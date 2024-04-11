#Understand the problem
'''
input: string of digits
output: number as an integer
explicit:
-cannot use the built in function int()
-Don't worry about leading char or invalid char. 
implicit:
questions:
Q:
A:
'''
#Examples and test cases
'''
print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True
'''
#Data structure
'''
dictionary'''
#Algorithm
'''
iterate through list and match each char with number
add number to corresponding decimal spot
return number'''
#Code
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


print(string_to_integer("4321"))  # True
print(string_to_integer("570") == 570)    # True