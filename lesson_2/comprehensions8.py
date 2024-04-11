dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

# [["Red", "Green"], "MEDIUM", ["Orange"], "LARGE"]

def transform(item):
    if item['type'] == 'fruit':
        return [color.capitalize() for color in item['colors']]
    else:
        return item['size'].upper()

new_list = [transform(item)
    for item in dict1.values()
]
print(new_list)