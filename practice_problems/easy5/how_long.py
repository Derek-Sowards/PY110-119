'''
input- string
output - list of words from string and each word followed by a space and words length
explicit - if string is empty or no argument, return an emtpy list

examples/test cases
data structure

algorithm
'''
def word_lengths(string=''):
    return [f'{word} {len(word)}'
            for word in string.split()]


print(word_lengths('cow sheep chicken'))
# ['cow 3', 'sheep 5', 'chicken 7']

print(word_lengths('baseball hot dogs and apple pie'))
# ['baseball 8', 'hot 3', 'dogs 4', 'and 3', 'apple 5', 'pie 3']

print(word_lengths("It ain't easy, is it?"))
# ['It 2', "ain't 5", 'easy, 5', 'is 2', 'it? 3']

print(word_lengths('Supercalifragilisticexpialidocious'))
# ['Supercalifragilisticexpialidocious 34']

print(word_lengths(''))      # []
print(word_lengths())        # []