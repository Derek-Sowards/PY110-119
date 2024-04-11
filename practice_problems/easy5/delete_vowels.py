'''
input- list of strings
output - list of strings with vowels removed

algorithm:
list comprehension with a function transformation
take_vowels function
    without_vowels = ''
iterate through characters in string
    if character not in vowels list
        append character to empty string'''

def remove_vowels(list_of_strings):
    return [take_vowels(element) for element in list_of_strings]

# def take_vowels(string):
#     without_vowels = ''
#     vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#     for char in string:
#         if char not in vowels:
#             without_vowels += char
#     return without_vowels

def take_vowels(string):
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in string if char not in vowels])


print(remove_vowels(['abcdefghijklmnopqrstuvwxyz']))        # ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(['green', 'YELLOW', 'black', 'white'])) # ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(['ABC', 'AEIOU', 'XYZ']))               # ['BC', '', 'XYZ']