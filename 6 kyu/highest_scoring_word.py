# Given a string of words, you need to find the highest scoring word.

# Each letter of a word scores points according to it's position in the alphabet: a = 1, b = 2, c = 3 etc.

# You need to return the highest scoring word as a string.

# If two words score the same, return the word that appears earliest in the original string.

# All letters will be lowercase and all inputs will be valid.

# https://www.codewars.com/kata/highest-scoring-word

import operator

def high(x):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    x_list = x.split()
    higher_word_list = []
    count = 0
    for word in x_list:
        count -= 1
        value = 0
        for letter in word:
            value = value + alphabet.index(letter) + 1
        higher_word_list.append([value, count, word])
    return sorted(higher_word_list, reverse=True, key=operator.itemgetter(0, 1))[0][2]