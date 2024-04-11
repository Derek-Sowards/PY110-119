'''
Understand the problem
input-list of integers
output- string rounded to three decimal places
explicit- string should be the result of multiplying all elements together and dividing by # of elements
implicit -
questions- what if list is empty?

Examples/ Test Cases

Data structures
    for loop
    value = 0

Algorithm
    set divisor to length of list
    set value to 0
    iterate through list
        multiply value to element
    divide value by divisor
    format integer with 3 decimals :.3f
    turn integer to string
    return string
'''
def multiplicative_average(lst):
    divisor = len(lst)
    value = 1
    for element in lst:
        value *= element
    average = value / divisor
    return f'{average:.3f}'

# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")