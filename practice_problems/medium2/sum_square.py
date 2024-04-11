'''
Understand the problem
input- integer
output- integer (difference of sum of digits **2 and the sum of digits squared individaully)
implicit:
will always be a positive number

examples/test cases

Data structure:
2 functions
for loops
count

Algorithm:
return squared_sum - squared_digits_sum

squared sum function:
    count = 0
    iterate through range of number + 1
    add those numbers to count
    return count ** count

squared_digits_sum
    count = 0
    iterate through range + 1
    add num * num to count
    return count
'''
def sum_square_difference(number):
    return squared_sum(number) - squared_digits_sum(number)

def squared_sum(number):
    number_sum = sum(range(1, number + 1))
    return number_sum * number_sum

def squared_digits_sum(number):
    count = 0
    for num in range(1, number + 1):
        count += num ** 2
    return count



print(sum_square_difference(3))      # 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)
print(sum_square_difference(10))     # 2640
print(sum_square_difference(1))      # 0
print(sum_square_difference(100))    # 25164150