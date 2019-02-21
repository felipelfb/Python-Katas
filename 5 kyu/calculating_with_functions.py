# This time we want to write calculations using functions and get the results. Let's have a look at some examples:

# JavaScript:

# seven(times(five())); // must return 35
# four(plus(nine())); // must return 13
# eight(minus(three())); // must return 5
# six(dividedBy(two())); // must return 3
# Ruby:

# seven(times(five)) # must return 35
# four(plus(nine)) # must return 13
# eight(minus(three)) # must return 5
# six(divided_by(two)) # must return 3
# Requirements:

# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby)
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function represents the right operand
# Divison should be integer division, e.g eight(dividedBy(three()))/eight(divided_by(three)) should return 2, not 2.666666...

# https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39

def zero(operation=None):
    if operation == None:
        return 0
    if operation[0] == 'plus':
        return operation[1]
    elif operation[0] == 'minus':
        return -operation[1]
    elif operation[0] == 'times':
        return 0
    elif operation[0] == 'divide':
        return 0
        
def one(operation=None):
    if operation == None:
        return 1
    if operation[0] == 'plus':
        return 1 + operation[1]
    elif operation[0] == 'minus':
        return 1 - operation[1]
    elif operation[0] == 'times':
        return operation[1]
    elif operation[0] == 'divide':
        return int(1/operation[1])
        
def two(operation=None):
    if operation == None:
        return 2
    if operation[0] == 'plus':
        return 2 + operation[1]
    elif operation[0] == 'minus':
        return 2 - operation[1]
    elif operation[0] == 'times':
        return 2 * operation[1]
    elif operation[0] == 'divide':
        return int(2/operation[1])
        
def three(operation=None):
    if operation == None:
        return 3
    if operation[0] == 'plus':
        return 3 + operation[1]
    elif operation[0] == 'minus':
        return 3 - operation[1]
    elif operation[0] == 'times':
        return 3 * operation[1]
    elif operation[0] == 'divide':
        return int(3/operation[1])
        
def four(operation=None):
    if operation == None:
        return 4
    if operation[0] == 'plus':
        return 4 + operation[1]
    elif operation[0] == 'minus':
        return 4 - operation[1]
    elif operation[0] == 'times':
        return 4 * operation[1]
    elif operation[0] == 'divide':
        return int(4/operation[1])
        
def five(operation=None):
    if operation == None:
        return 5
    if operation[0] == 'plus':
        return 5 + operation[1]
    elif operation[0] == 'minus':
        return 5 - operation[1]
    elif operation[0] == 'times':
        return 5 * operation[1]
    elif operation[0] == 'divide':
        return int(5/operation[1])
        
def six(operation=None):
    if operation == None:
        return 6
    if operation[0] == 'plus':
        return 6 + operation[1]
    elif operation[0] == 'minus':
        return 6 - operation[1]
    elif operation[0] == 'times':
        return 6 * operation[1]
    elif operation[0] == 'divide':
        return int(6/operation[1])
        
def seven(operation=None):
    if operation == None:
        return 7
    if operation[0] == 'plus':
        return 7 + operation[1]
    elif operation[0] == 'minus':
        return 7 - operation[1]
    elif operation[0] == 'times':
        return 7 * operation[1]
    elif operation[0] == 'divide':
        return int(7/operation[1])
        
def eight(operation=None):
    if operation == None:
        return 8
    if operation[0] == 'plus':
        return 8 + operation[1]
    elif operation[0] == 'minus':
        return 8 - operation[1]
    elif operation[0] == 'times':
        return 8 * operation[1]
    elif operation[0] == 'divide':
        return int(8/operation[1])
        
def nine(operation=None):
    if operation == None:
        return 9
    if operation[0] == 'plus':
        return 9 + operation[1]
    elif operation[0] == 'minus':
        return 9 - operation[1]
    elif operation[0] == 'times':
        return 9 * operation[1]
    elif operation[0] == 'divide':
        return int(9/operation[1])

def plus(right_operand):
    operation = []
    operation.append('plus')
    operation.append(right_operand)
    return operation
    
def minus(right_operand):
    operation = []
    operation.append('minus')
    operation.append(right_operand)
    return operation
    
def times(right_operand):
    operation = []
    operation.append('times')
    operation.append(right_operand)
    return operation
    
def divided_by(right_operand):
    operation = []
    operation.append('divide')
    operation.append(right_operand)
    return operation