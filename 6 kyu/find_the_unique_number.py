# There is an array with some numbers. All numbers are equal except for one. Try to find it!

# findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
# findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55
# It’s guaranteed that array contains more than 3 numbers.

# The tests contain some very huge arrays, so think about performance.

# https://www.codewars.com/kata/find-the-unique-number-1/train/python

def find_uniq(arr):
    n1 = arr[0]
    n2 = arr[1]
    if n1 != n2:
        n3 = arr[2]
        if n3 == n1:
            return n2
        else:
            return n1
    for number in range(2, len(arr)):
        n3 = arr[number]
        if n3 != n1:
            return n3