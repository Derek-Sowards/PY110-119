'''
Understand the Problem:
input- String
output- Boolean
explicit- Return True if parenthesis are properly balanced
        Properly balanced = parenthesis must occur in matching ( )
implicit- must have ( and a ) to close it off. if not, it is not properly balanced
Questions- what if there are no parenthesis at all? ---> return True


Examples/Test Cases

Data structure:
counter

Algorithm
set a counter to 0
iterate through each character in the list
    if there is a ( add 1 to the counter
    if there is a ) subtract 1 from the counter
    else none
return counter == 0
'''
def is_balanced(string):
    counter = 0
    for char in string:
        if char == '(':
            counter += 1
        elif char == ')':
            counter -= 1
        if counter < 0:
            return False
    return counter == 0


print(is_balanced("What (is) this?") == True)
print(is_balanced("What is) this?") == False)
print(is_balanced("What (is this?") == False)
print(is_balanced("((What) (is this))?") == True)
print(is_balanced("((What)) (is this))?") == False)
print(is_balanced("Hey!") == True)
print(is_balanced(")Hey!(") == False)
print(is_balanced("What ((is))) up(") == False)