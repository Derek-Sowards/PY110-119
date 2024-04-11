'''
input - list of integers
output - integer (sum of sums)

data structure:

algorithm:
sum = 0
iterate through list
    add sum with element multiplied by length of list
return sum
'''
def sum_of_sums(list):
    sum = 0
    for idx in range(len(list)):
        sum += list[idx] * (len(list[idx:]))
    return sum


print(sum_of_sums([3, 5, 2]))        # (3) + (3 + 5) + (3 + 5 + 2) --> 21
print(sum_of_sums([1, 5, 7, 3]))     # (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36
print(sum_of_sums([4]))              # 4
print(sum_of_sums([1, 2, 3, 4, 5]))  # 35