# lst1 = ['a', 'b', ['c', ['d', 'e', 'f', 'g']]]
# letter_g = lst1[2][1][3]
# print(letter_g)

# lst2 = [
#     {
#         'first': ['a', 'b', 'c'],
#         'second': ['d', 'e', 'f']
#     },
#     {
#         'third': ['g', 'h', 'i']
#     }
# ]
# letter_g = lst2[1]['third'][0]
# print(letter_g)

# lst3 = [['abc'], ['def'], {'third': ['ghi']}]
# letter_g = lst3[2]['third'][0][0]--------?
# print(letter_g)

# dict1 = {'a': ['d', 'e'], 'b': ['f', 'g'], 'c': ['h', 'i']}
# letter_g = dict1['b'][1]--------?
# print(letter_g)

dict2 = {'1st': {'d': 3}, '2nd': {'e': 2, 'f': 1}, '3rd': {'g': 0}}
letter_g = list(dict2['3rd'].keys())[0]
print(letter_g)