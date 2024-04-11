dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}
vowels = 'aeiou'

# list_of_vowels = []

# for key in dict1:
#     for word in dict1[key]:
#         for letter in word:
#             if letter in vowels:
#                 list_of_vowels.append(letter)

list_of_vowels = [letter
    for key in dict1
    for word in dict1[key]
    for letter in word
    if letter in vowels
]

print(list_of_vowels)
# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']