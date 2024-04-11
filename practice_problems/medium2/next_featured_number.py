'''
Understand the problem:
input- integer
output- integer (next featured number)
explicit:
-featured # = odd # that is a multiple of 7, with all digits occuring exactly once
-issue error message if there is no next feature number
-The largest possible featured number is 9876543201

examples/test cases

Data structure:
for loop

algorithm:
set max number to 9876543201
for num in range(input_num) to max number
    if num % 7 == 0 and occur_once(num)
        return num
return "error, # can't occur"

def occur_once(num)
    return set(str(num)) == len(str(num))
'''
def featured(input_num):
    max_num = 9876543201
    for num in range(input_num + 1, max_num + 1):
        if num % 7 == 0 and occur_once(num) and num % 2 != 0:
            return num
    return "Error, # can't occur"

def occur_once(number):
    return len(set(str(number))) == len(str(number))

print(featured(12))           # 21
print(featured(20))           # 21
print(featured(21))           # 35
print(featured(997))          # 1029
print(featured(1029))         # 1043
print(featured(999999))       # 1023547
print(featured(999999987))    # 1023456987
print(featured(9876543186))   # 9876543201
print(featured(9876543200))   # 9876543201
print(featured(9876543201))   # "There is no possible number that fulfills those requirements."