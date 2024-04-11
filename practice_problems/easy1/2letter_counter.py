def word_sizes(string):
    split_str = string.split()
    word_size_dict = {}

    for word in split_str:
        clean_word = clean_str(word)
        if len(clean_word) not in word_size_dict.keys():
            word_size_dict[len(clean_word)] = 1
        else:
            word_size_dict[len(clean_word)] += 1
    return word_size_dict

def clean_str(string):
    cleansed = ''
    for char in string:
        if char.isalpha():
            cleansed += char
    return cleansed
# def clean_str(lst):
#     return 
# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})