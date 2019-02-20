# There is an array of strings. All strings contains similar letters except one. Try to find it!

# find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) # => 'BbBb'
# find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) # => 'foo'
# Strings may contain spaces. Spaces is not significant, only non-spaces symbols matters. E.g. string that contains only spaces is like empty string.

# It’s guaranteed that array contains more than 3 strings.

# https://www.codewars.com/kata/find-the-unique-string/train/python

def find_uniq(arr):
    string1 = get_char_dict(arr[0])
    string2 = get_char_dict(arr[1])
    if string1 != string2:
        string3 = get_char_dict(arr[2])
        if string3 == string1:
            return arr[1]
        else:
            return arr[0]
    for string in range(2, len(arr)):
        string3 = get_char_dict(arr[string])
        if string3 != string1:
            return arr[string]

def get_char_dict(string):
    char_dict = {}
    for char in string:
        if char.lower() not in char_dict and char != ' ':
            char_dict[char.lower()] = 1
    return char_dict