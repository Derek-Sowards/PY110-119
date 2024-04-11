def substrings(string):
    all_substrings = []

    for idx in range(len(string)):
        result = ''
        for char in string[idx:]:
            result += char
            all_substrings.append(result)

    return all_substrings



print(substrings('abc'))
print()
print(substrings('abcde'))

# prints
# [ "a", "ab", "abc", "abcd", "abcde",
#  "b", "bc", "bcd", "bcde",
#  "c", "cd", "cde",
#  "d", "de",
#  "e" ]