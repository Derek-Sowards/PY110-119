def signed_integer_to_string(number):
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
    is_positive = number > 0
    
    if not is_positive:
        number *= -1
        #or number = abs(number)

    while number != 0:
        last_number = number % 10
        last_number_str = conversion_dict[last_number]
        string_to_return += last_number_str
        number //= 10
        
    if is_positive:
        string_to_return += '+'
    else:
        string_to_return += '-'
    return string_to_return[::-1]

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True