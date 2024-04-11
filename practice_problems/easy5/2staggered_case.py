'''
every other alphabetical character should be capitlized

algorithm
set an empty string to return
set upper_toggle = True
iterate through char in string
    if char is alphabetic
        if upper is true
            add char.capitalize to result
        else:
            add char.lower to result
        upper_toggle = not upper_toggle
    else:
        add char to result
return result

'''
def staggered_case(string):
    staggered = ''
    toggle = True
    for char in string:
        if char.isalpha():
            if toggle:
                staggered += char.capitalize()
            else:
                staggered += char.lower()
            toggle = not toggle
        else:
            staggered += char
    return staggered


print(staggered_case("I Love Launch School!") == "I lOvE lAuNcH sChOoL!")
print(staggered_case("ALL CAPS") == "AlL cApS")
print(staggered_case("ignore 77 the 444 numbers") == "IgNoRe 77 ThE 444 nUmBeRs")