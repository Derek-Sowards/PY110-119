def reverse_string(s):
    y = ''
    for char in s:
        y = char + y
    return y

print(reverse_string("hello"))