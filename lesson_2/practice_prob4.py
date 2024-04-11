munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}
# (name) is a (age)-year-old (male or female).
for name in munsters:
    print(f"{name} is a {munsters[name]['age']}-year-old {munsters[name]['gender']}")