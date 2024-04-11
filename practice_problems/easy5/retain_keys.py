'''
input - dictionary, list of keys 
output- dictionary with just specified keys

dict comprehension

'''
def keep_keys(dict, keys):
    return {key: value for key, value in dict.items() if key in keys}


print(keep_keys({'red': 1, 'green': 2, 'blue': 3, 'yellow': 4}, ['red', 'blue']))
# {'red': 1, 'blue': 3}