#Understand the Problem
'''
input: string of words separated by spaces
output: string of words with first and last letters swapped
implicit:
explicit:
-every word will contain at least 1 letter
-every string will contain at least 1 word
-just letters separated by whitespace. no leading or trailing whitespace
questions
Q:do capital letters matter?
A: no they do not
'''
#Examples and test cases
'''
print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True
'''
#Data structure
'''
function
list
'''
#Algorithm
'''
split string into separate words
replace the first and last letter of word
add word to flipped_string
repeat until finished
return flipped_string
'''
def swap(string):
    cut_string = string.split()
    swapped_string_list = []

    for word in cut_string:
        swapped_string_list.append(swap_letters(word))

    return ' '.join(swapped_string_list)

def swap_letters(word):
    if len(word) == 1:
        return word
    return word[-1] + word[1:-1] + word[0]





def swap(string):
    words_list = string.split()

    for idx in range(len(words_list)):
        words_list[idx] = swap_first_and_last(words_list[idx])
    
    return ' '.join(words_list)

def swap_first_and_last(word):
    if len(word) == 1:
        return word
    return word[-1] + word[1:-1] + word[0]

print(swap('Oh what a wonderful day it is'))  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True