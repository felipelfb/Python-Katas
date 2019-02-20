# Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer. You don't need to validate the form of the Roman numeral.

# Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately, starting with the leftmost digit and skipping any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.

# Example:

# solution('XXI') # should return 21
# Help:

# Symbol    Value
# I          1
# V          5
# X          10
# L          50
# C          100
# D          500
# M          1,000
# Courtesy of rosettacode.org

# https://www.codewars.com/kata/roman-numerals-decoder/python

def solution(roman):
    roman_dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    previous_digit = roman[0]
    value = roman_dict[previous_digit]
    for digit in range(1, len(roman)):
        current_digit = roman[digit]
        if roman_dict[current_digit] > roman_dict[previous_digit]:
            value = value - roman_dict[previous_digit] + roman_dict[current_digit] - roman_dict[previous_digit]
        else:
            value += roman_dict[current_digit]
    return value