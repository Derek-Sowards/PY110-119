munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}
# total_age = 0
# for element in munsters.values():
#     if element['gender'] == 'male':
#         total_age += element['age']
# print(total_age)

total_age = [element['age']
    for element in munsters.values()
    if element['gender'] == 'male'
]
print(sum(total_age))