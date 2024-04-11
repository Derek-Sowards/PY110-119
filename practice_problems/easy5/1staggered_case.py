'''
input- string
output- string with every other character capitalized
explicit- 
Non-alphabetic characters should not be changed, but should be counted as characters
 for determining when to switch between upper and lower case.

examples/test cases
 
Data structure:
empty string
possible list comp

Algorithm:
iterate through string
    if index is even and alphabetical
        capitalize character
    else:
        add character
return new string

'''
def staggered_case(string):
    # transformed_string = ''
    # for idx, char in enumerate(string):
    #     if idx % 2 == 0 and char.isalpha():
    #         transformed_string += char.capitalize()
    #     else:
    #         transformed_string += char.lower()
    # return transformed_string
    return ''.join([char.capitalize() if idx % 2 == 0 else char.lower()
        for idx, char in enumerate(string)
    ])




print(staggered_case('I Love Launch School!'))        # "I LoVe lAuNcH ScHoOl!"
print(staggered_case('ALL_CAPS'))                     # "AlL_CaPs"
print(staggered_case('ignore 77 the 4444 numbers'))   # "IgNoRe 77 ThE 4444 nUmBeRs"