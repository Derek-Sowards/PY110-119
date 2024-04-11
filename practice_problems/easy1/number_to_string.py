#Understand the Problem
'''
input: number
output: string
explicit:
-cannot use str() function
'''
#Similar to previous two exercises, so going to jump right into code

def integer_to_string(number):
    if number == 0:
        return '0'
    
    conversion_dict = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
    }
    string_to_return = ''

    while number != 0:
        last_number = number % 10
        last_number_str = conversion_dict[last_number]
        string_to_return += last_number_str
        number //= 10
    
    return ''.join(reversed(list(string_to_return)))
    #or return string_to_return[::-1]



print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True