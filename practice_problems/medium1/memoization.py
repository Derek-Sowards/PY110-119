
look_up_table = {}
def fibonacci(num):
    if num < 2:
        return num
    elif num in look_up_table:
        return look_up_table[num]
    else:
        look_up_table[num] = (fibonacci(num -1) + fibonacci(num -2))
    return look_up_table[num]