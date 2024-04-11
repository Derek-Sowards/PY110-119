def swap_name(string):
    name_list = string.split()
    return str(name_list[1] + ', ' + name_list[0])


print(swap_name('Joe Roberts'))    # "Roberts, Joe"