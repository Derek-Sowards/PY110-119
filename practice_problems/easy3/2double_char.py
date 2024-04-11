
'''Algorithm
    create an empty string
    create a vowel list
    for character in string
        if char not in vowel and not char.isalpha
            add char * 2 to empty string
        else
            add char to empty string
'''
# All of these examples should print True
def double_consonants(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    doubled_string = ''
    for char in string:
        if char not in vowels and char.isalpha():
            doubled_string += char * 2
        else:
            doubled_string += char
    return doubled_string

print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")