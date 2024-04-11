#Understand the Problem
"""
input: List of strings
output: list of sorted strings (new object)
initial questions?:
-is case important???
-will the list of strings be all lowercase?, if not, do I return a new list with 
all lowercase? (*strings are all lowercase*)
-will there be empty lists???
-how will i handle non string objects in the list???
-How should the list be sorted? ascending or descending? (*highest to lowest*)
-Is it possible for a string to contain no adjacent consonants? (*yes*)
-How do i treat the letter y? as a constant? or a vowel?

implicit:
-strings may contain 1 or multiple words
-strings may not be empty
-strings should be sorted in descending order (highest to lowest)
-input list should always be strings
-case is not relevant
-don't mutate the original list, but rather return a new object
-Returned list goes from HIGHEST CONSONANT count to lowest.
- Single consonants in a string do not affect sort order in
  comparison to strings with no consonants. Only adjacent
  consonants affect sort order.

explicit:
-return list of sorted strings by highest number of non vowels next to each other
-if two strings contain the the same number of non vowels, they should retain
their original order in relation to each other
-constants are adjacent if touching, or if white space separates them

"""
#Exmaples and test cases
"""
my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']

3 questions left
"""
#Data type
"""
-Data type must retain order. (LIST)
-must return a LIST
-maybe a dictionary to keep track of string and adjc constant count
"""
#Algorithm. (high level abstract plan)
"""
1. For each string in the input list, determine the highest number
   of adjacent consonants within that string.
2. Sort the input list based on the calculated highest number of
   consonants from step 1.
3. Return the sorted list.
----
-create an empty list to return
-create a count of 0 adjc consonates for every string in the list
-iterate through each string and count # of adj constants
-update consonate count with correct number
-compare each consonate count to the others, appending highest count to LIST
    -if two lists share same adj consonate, the first in list gets appended. 
-return new list in descending order.


(sub function)
Given a string, return a count of the highest number of adjacent
 consonants anywhere in that string
 Input: a string
Output: an integer representing a count of the highest number of
        adjacent consonants in the string

-initialize an empty string
-take out any white space characters in the string
-iterate through each letter of the string
-if the letter is not a vowel, and the previous letter is a constant append it to the empty string
-figure the length of the newly created string
-return that length



- For each "letter" in the "input string":
    - If the "letter" is a consonant:
        - Concatenate it to the "adjacent consonants string".
    - If the "letter" is a vowel:
        - If the "adjacent consonants string" has a length
          greater than the current "maximum consonants count":
            - If the "adjacent consonants string" has a length
              greater than 1:
                - Set the "maximum consonants count" to the length
                  of the "adjacent consonants string".

        - Reset the "adjacent consonants string" to an empty string.

- Return the "maximum consonants count".
"""
#Code

def count_consonates(str):
    adjacent_constants = ''
    no_space_string = str.replace(' ', '')
    max_count = 0
    for char in no_space_string:
        if char not in ['a', 'e', 'i', 'o', 'u']:
            adjacent_constants += char
            if len(adjacent_constants) > max_count:
                if len(adjacent_constants) > 1:
                    max_count = len(adjacent_constants)
        else:
            if len(adjacent_constants) > max_count:
                if len(adjacent_constants) > 1:
                    max_count = len(adjacent_constants)

            adjacent_constants = ''
    return max_count

def sort_by_consonant_count(lst):
    lst.sort(key=count_consonates, reverse=True)
    return lst



# my_list = ['aa', 'baa', 'ccaa', 'dddaa']
# print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

# my_list = ['can can', 'toucan', 'batman', 'salt pan']
# print(sort_by_consonant_count(my_list))
# # ['salt pan', 'can can', 'batman', 'toucan']

# my_list = ['bar', 'car', 'far', 'jar']
# print(sort_by_consonant_count(my_list))
# # ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']