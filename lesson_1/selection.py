# produce = {
#     'apple': 'Fruit',
#     'carrot': 'Vegetable',
#     'pear': 'Fruit',
#     'broccoli': 'Vegetable',
# }

# def select_fruit(dct):
#     updated_dict = {}
#     for key, value in dct.items():
#         if value == 'Fruit':
#             updated_dict[key] = value
#     return updated_dict


# print(select_fruit(produce))  # { apple: 'Fruit', pear: 'Fruit' }
#-----
# def double_numbers(numbers):
#     for idx in range(len(numbers)):
#         numbers[idx] *= 2
#     return numbers

# my_numbers = [1, 4, 3, 7, 2, 6]
# print(double_numbers(my_numbers)) # [2, 8, 6, 14, 4, 12]
# print(my_numbers)                 # [1, 4, 3, 7, 2, 6]
#-----
# def double_odd_indices(lst):
#     for idx in range(len(lst)):
#         if idx % 2 != 0:
#             lst[idx] *= 2
#     return lst

# my_numbers = [1, 4, 3, 7, 2, 6]
# print(double_odd_indices(my_numbers))

# # not mutated
# print(my_numbers)
#-----
# def double_odd_indices(lst):
#     doubled_list = []
#     for idx in range(len(lst)):
#         current_number = lst[idx]
#         if idx % 2 != 0:
#             doubled_list.append(current_number *2)
#         else:
#             doubled_list.append(current_number)
#     return doubled_list

# my_numbers = [1, 4, 3, 7, 2, 6]
# print(double_odd_indices(my_numbers))

# # not mutated
# print(my_numbers)
#-----
# def multiply(number_list, int_to_multiply):
#     multiplied_list = []

#     for num in number_list:
#         multiplied_list.append(num * int_to_multiply)
#     return multiplied_list

# my_numbers = [1, 4, 3, 7, 2, 6]
# print(multiply(my_numbers, 3))  # [3, 12, 9, 21, 6, 18]
# #-----

# statement = "The Flintstones Rock"

# dict = {}
# squished_statement = statement.replace(' ', '')
# for char in squished_statement:
#     dict[char] = dict.get(char, 0) + 1
# print(dict)

# def frequency(string):
#     squished_string = string.replace(' ', '')
#     updated_dict = {}
#     for char in squished_string:
#         if char not in updated_dict:
#             updated_dict[char] = 1
#         else:
#             updated_dict[char] += 1
#     return updated_dict

# print(frequency(statement))
#-----
