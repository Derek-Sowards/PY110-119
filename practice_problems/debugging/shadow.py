def sum_function(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(sum_function(numbers, 2) == 20)