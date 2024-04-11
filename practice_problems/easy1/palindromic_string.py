#Understand the problem
'''
input: string
output: Boolean 
implicit:
explicit:
-A palindrome reads the same forwards and backwards
-Return True if string is palindrome, False otherwise
-Case/Characters matter
questions:
-Will the string ever be empty?
'''
#Write examples/ test cases
'''
# All of these examples should print True
print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)
# case matters
print(is_palindrome('Madam') == False)
# all characters matter
print(is_palindrome("madam i'm adam") == False)
'''
#Data Structure
"""
function
"""
#Algorithm
"""
Cut string into two
reverse one of the sub strings
Return True or False depending if the two substrings match eachother.
"""
def is_real_palindrome(s):
    cleaned_string = ''
    for char in s:
        if char.isalnum() and char.isascii():
            cleaned_string += char.casefold()
    return is_palindrome(cleaned_string)

def is_palindrome(s):
    return s == s[::-1]



print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True

# def is_palindrome(s):
#     return s == s[::-1]

# # All of these examples should print True

# print(is_palindrome('madam') == True)
# print(is_palindrome('356653') == True)
# print(is_palindrome('356635') == False)

# # case matters
# print(is_palindrome('Madam') == False)

# # all characters matter
# print(is_palindrome("madam i'm adam") == False)