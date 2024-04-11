#Understand the Problem
'''
input: string
output: dictionary showing number of words of different sizes
implicit:
-empty string returns empty dict
-any character that isn't white space, counts as words length
explicit:
-if multiple words have same length, should show in dict
questions:

'''
#Create examples/ test cases
'''
# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})
'''
#Data structure
'''
dictionary comprehension?
inside function
'''
#Algorithm
'''
-cut string up by white space
-count characters in each cut word
-add to dictionary
-return dict
'''
#Code
def word_sizes(string):
    split_str = string.split()
    word_size_dict = {}
    for word in split_str:
        if len(word) not in word_size_dict.keys():
            word_size_dict[len(word)] = 1
        else:
            word_size_dict[len(word)] += 1
    return word_size_dict
            


# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})