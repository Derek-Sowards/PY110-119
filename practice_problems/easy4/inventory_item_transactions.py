'''
input- inventory item id #, and list of transactions (101, transactions)
output- list containing transactions for specified id within list

examples/test cases

Data structure
possible a list comprehension

Algorithm
iterate through every element in list
    if id key is 101
        add it to return list
return list
'''
def transactions_for(id, list):
    return [element for element in list
            if element['id'] == id]

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

print(transactions_for(101, transactions))
# prints
# [ {"id": 101, "movement": "in",  "quantity":  5},
#   {"id": 101, "movement": "in",  "quantity": 12},
#   {"id": 101, "movement": "out", "quantity": 18} ]