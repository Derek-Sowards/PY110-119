lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]
def only_multiples(sublist):
    # multiples_list = []
    # for number in sublist:
    #     if number % 3 == 0:
    #         multiples_list.append(number)
    # return multiples_list
    return [number for number in sublist if number % 3 == 0]

new_lst = [only_multiples(sublist)
    for sublist in lst
]
print(new_lst)