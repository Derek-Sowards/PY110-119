'''
input- item Id, list of transactions
output- Boolean based on if there is available items in inventory

algorithm:
get all elements that have the specified item id
pass those elements to a function 
inventory = 0
if movement is in, increase inventory
if movement is out, decrease inventory
return inventory > 0
'''
def is_item_available(id, list):
    all_transactions = [element for element in list
            if element['id'] == id]
    
    return calculate_inventory(all_transactions)

def calculate_inventory(list_of_transactions):
    quantity = 0
    for element in list_of_transactions:
        if element['movement'] == 'in':
            quantity += element['quantity']
        else:
            quantity -= element['quantity']
    return quantity > 0

transactions = [ {"id": 101, "movement": 'in',  "quantity":  5},
                 {"id": 105, "movement": 'in',  "quantity": 10},
                 {"id": 102, "movement": 'out', "quantity": 17},
                 {"id": 101, "movement": 'in',  "quantity": 12},
                 {"id": 103, "movement": 'out', "quantity": 20},
                 {"id": 102, "movement": 'out', "quantity": 15},
                 {"id": 105, "movement": 'in',  "quantity": 25},
                 {"id": 101, "movement": 'out', "quantity": 18},
                 {"id": 102, "movement": 'in',  "quantity": 22},
                 {"id": 103, "movement": 'out', "quantity": 15}]

print(is_item_available(101, transactions))  # False
print(is_item_available(103, transactions))  # False
print(is_item_available(105, transactions))  # True