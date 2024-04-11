'''Understand the problem
input- two integers. 1st integer is count, 2nd is starting number of your sequence
output- list containing same # of elements as count, each element is multiple of starting#
explicit- count will always be 0 or greater, if count is 0, should return empty list

Examples/Test Cases

'''
def sequence(count, step):
    return_list = []
    for idx in range(1, count +1):
        return_list.append(step * idx)
    return return_list

print(sequence(5, 1))          # [1, 2, 3, 4, 5]
print(sequence(4, -7))         # [-7, -14, -21, -28]
print(sequence(3, 0))          # [0, 0, 0]
print(sequence(0, 1000000))    # []