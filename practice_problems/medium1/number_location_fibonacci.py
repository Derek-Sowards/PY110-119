import sys

def find_fibonacci_index_by_length(num_length):
    sys.set_int_max_str_digits(50_000)
    first = 1
    second = 1
    count = 2

    while len(str(second)) < num_length:
        first, second = second, first + second
        count += 1
    
    return count
    


# All of these examples should print True
# The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
print(find_fibonacci_index_by_length(1000) == 4782)
print(find_fibonacci_index_by_length(10000) == 47847)