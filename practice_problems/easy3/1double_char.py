'''
Understand the problem:
input- string 'hello'
output- string with each character doubled 'hheelllloo'
explicit
questions- will the string ever be empty? If string, empty return empty string

Examples/Test Cases
Data structure:
for loop
empty string

Algorithm:
    create return string
    for char in input_string
        append 2 of char to return string
    return return string
'''
'''
def repeater(string):
    return_string = ''
    for char in string:
        return_string += char + char
    return return_string
'''

def repeater(string):
    return ''.join([char * 2 for char in string])

print(repeater('Hello'))        # "HHeelllloo"
print(repeater('Good job!'))    # "GGoooodd  jjoobb!!"
print(repeater(''))             # ""