lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]
def sum_of_odds(sublist):
    odd_numbers = [number for number in sublist if number % 2 != 0]
    return sum(odd_numbers)

sorted_list = sorted(lst, key=sum_of_odds)
print(sorted_list)