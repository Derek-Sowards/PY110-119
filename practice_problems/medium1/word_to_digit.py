'''

Algorithm
create an empty string
loop through element in split string
    match statement
    if statement matches case
        append digit string to empty string
    case _:
        append element
return empty string
'''
def word_to_digit(string):
    result = ''

    for word in string.split():
        match word:
            case 'zero':
                result += ' 0'
            case 'one':
                result += ' 1'
            case 'two':
                result += ' 2'
            case 'three':
                result += ' 3'
            case 'four':
                result += ' 4'
            case 'five':
                result += ' 5'
            case 'six':
                result += ' 6'
            case 'seven':
                result += ' 7'
            case 'eight':
                result += ' 8'
            case 'nine':
                result += ' 9'
            case _:
                result += f' {word}'
    return result.lstrip()


message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True