'''
input- positive int (23)
output- integer (sum of input digits 2 + 3)

examples/test cases
data structure:
list comprehension

algorithm:
cut up the integer into separate digits
    turn into string

add all digits together
return sum

'''

def sum_digits(number):
    return sum([int(char) for char in str(number)])



print(sum_digits(23))           # 5
print(sum_digits(496))          # 19
print(sum_digits(123456789))    # 45