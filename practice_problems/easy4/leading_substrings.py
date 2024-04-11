''''
input- string
output- list of substrings
explicit - each substring should start with the first letter of the string
        ordered from shortest to longest substring

examples/test cases
data structure:

algorithm
create an empty list subtrings
for each character of string
    create substring
    if substring not in list
        append substring to list
return substrings

code:'''

def leading_substrings(string):
    substrings = []
    for char in string:
        if len(substrings) == 0:
            substrings.append(char)
        else:
            substring = substrings[-1] + char
            if substring not in substrings:
                substrings.append(substring)
    return substrings


print(leading_substrings('abc'))      # ['a', 'ab', 'abc']
print(leading_substrings('a'))        # ['a']
print(leading_substrings('xyzzy'))    # ['x', 'xy', 'xyz', 'xyzz', 'xyzzy']