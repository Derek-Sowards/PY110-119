'''
Understand the problem
input - string
output -object containing following 3 properties
1. percentage of characters in the string that are lowercase letters
2. percentage of characters that are uppercase letters
3. percentage of characters that are neither
explicit:
string will always contain 1 letter
implicit:
if one of three is not present, number should be 0
numbers should be formatted 2 digits after the decimal point

examples/test cases:

data structure:
dictionary

algorithm:
create a dictionary with lowercase, uppercase, neither keys
find the length of the string
iterate through string
    if char is char.lowercase()
        add an int(char) to dictionary key value
    if char is char.upper()
        add int() to dictionary key value
    else:
        add char to dictionary key value neither
list comprehension, changing the value//2 to a string with proper formatting

'''
def letter_percentages(string):
    ratio_dictionary = {'lowercase': 0, 'uppercase': 0, 'neither': 0}
    string_length = len(string)
    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for char in string:
        if char in lower_case:
            ratio_dictionary['lowercase'] += 1
        elif char in upper_case:
            ratio_dictionary['uppercase'] += 1
        else:
            ratio_dictionary['neither'] += 1
    return {key: f'{find_percentage(value, string_length):.2f}'
        for key, value in ratio_dictionary.items()
    }

def find_percentage(num, string_length):
    if num == 0:
        return 0.00
    return (num/string_length) * 100


print(letter_percentages('abCdef 123'))
# { 'lowercase': "50.00", 'uppercase': "10.00", 'neither': "40.00" }

print(letter_percentages('AbCd +Ef'))
# { 'lowercase': "37.50", 'uppercase': "37.50", 'neither': "25.00" }

print(letter_percentages('123'))
# { 'lowercase': "0.00", 'uppercase': "0.00", 'neither': "100.00" }