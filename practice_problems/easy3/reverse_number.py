'''
Understand the problem
input - integer 54321
output - reversed number 12345
explicit
Q - what about trailing zeros?

Examples/test cases

data structure:
str(), and int(), reverse(), list comprehension?

algorithm
turn int into string
reverse string
strip leading 0's
return int of string

'''
def reverse_number(input_num):
    return int(str(input_num)[::-1].lstrip('0'))

def reverse_number(number):
    return int(str(number)[::-1])

print(reverse_number(12345))    # 54321
print(reverse_number(12213))    # 31221
print(reverse_number(456))      # 654
print(reverse_number(12000))    # 21 # Note that leading zeros in the result get dropped!
print(reverse_number(1))        # 1