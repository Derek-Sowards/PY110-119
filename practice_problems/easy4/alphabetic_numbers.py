'''
Understand the problem
input- list of integer
output- list of integers sorted based off their name in english

examples/test cases

Data stucture:
list and indexing

algorithm
create a list with all the english words 0-19
create a function that returns the word for each #
create a function that sorts the numbers based off that function key

'''
WORDS_LIST = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
              'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
              'seventeen', 'eighteen', 'nineteen']

def word_to_number(number):
    return WORDS_LIST[number]

def alphabetic_number_sort(numbers):
    return sorted(numbers, key=word_to_number)

print(alphabetic_number_sort(
   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]))
# [8, 18, 11, 15, 5, 4, 14, 9, 19, 1, 7, 17, 6, 16, 10, 13, 3, 12, 2, 0]