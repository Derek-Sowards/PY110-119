#Givenn a dictionary, return a its keys in an ordered list, based on the values

def order_by_value(dict):
    sorted_items = sorted(dict.items(), key=get_value)
    return [key for key, value in sorted_items]

def get_value(item):
    return item[1]

print(order_by_value({'p': 8, 'q': 2, 'r': 6}))
# ['q', 'r', 'p']