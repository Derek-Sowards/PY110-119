'''
Understand the Problem
input-string
output-list of all palindromic substrings of that string
explicit- substrings must be sorted based on their appearance of string
        -duplicate substrings should be included multiple times
        -single characters are not substrings
questions- are substrings case sensitive? yes

Examples and Test Cases

Data structure
lists
1 function to find all substrings
2 function to then test if each substring is palindromic

Algorithm
create a function to find all the substrings in a string

create a function to test if a substring is palindromic
    return string if string == string[::-1]
'''
def substrings(string):
    substrings = []

    for idx in range(len(string)):
        result = ''
        for char in string[idx:]:
            result += char
            substrings.append(result)
    return substrings

def palindromes(string):
    list_of_substrings = substrings(string)
    return[substring 
           for substring in list_of_substrings
            if substring == substring[::-1] and len(substring) != 1]

print(palindromes('madam'))
print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True