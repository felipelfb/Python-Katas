# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, and u as vowels for this Kata.

# The input string will only consist of lower case letters and/or spaces.

# https://www.codewars.com/kata/54ff3102c1bad923760001f3

def getCount(inputStr):
    num_vowels = 0
    vowels = ["a","e","i","o","u","á","à","ã","é","í","ó","õ","ú"]
    for index in range(len(inputStr)):
        if inputStr[index].lower() in vowels:
            num_vowels = num_vowels + 1
    
    return num_vowels