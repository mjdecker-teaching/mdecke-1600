##
# @file data_structures.py
#
# Data structures in Python based on: https://docs.python.org/3/tutorial
#
# @author Michael John Decker, Ph.D.
#

# What are the basic operations of a stack
# top, push, pop
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)

tos = stack[-1]
print(tos)

tos = stack.pop()
print(tos)
print(stack)

# What type of structure is stack
# LIFO

# How do you categorize a queue
# FIFO (techically, stack is a LIFO queue)
# What are the operations of a queue?
# enqueue(), first(), dequeue()
# So, list is not effifcient for a queue so will use a deque
from collections import deque
queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)
print(queue)

first = queue[0]
print(first)

first = queue.popleft()
print(first)
print(queue)

# So, how might you go about generating a list of the 20 powers of 2 (up to 2 ** 20)
powers = []
for i in range(21) :
    powers.append(2 ** i)
print powers

# Python has more power syntax for generating lists
# First is we could use maps and lambdas
# These have roots in functional languages
# A llambda is an anyonymous (or unamed function).  The syntax is:
#lambda param: expression

# We can assign them to variables and parameters, and call them
func = lambda i: 2 ** i
func(3)

# map takes a list and applies a function to each element in an iterable sequence and returns a list
values = [1, 2, 3]
powers =  map(func, values)
print(values)
# actually a map object, use function style cast
print(powers)
print(list(powers))

# Lets combine this syntax
powers = list(map(lambda i: 2 ** i, range(21)))


# Python has an even more power syntax called list-comprehensions
# The form is
#[expression for identifier in sequence]
powers = [2 ** i for i in range(21)]
print(powers)

# How might we use this to generate a list of first 10 cubes?
cubes = [i ** 3 for i in range(10)]
print(cubes)

# The actual syntax is a bit longer
# you can have additional for and if clauses
# For example, cartesian product (as tuples)
product = [(x, y) for x in [1, 2, 3] for y in [3, 2, 1]]
print(product)

# So, if come into play when you want to place restrictions
# such as don't want when x == y
product = [(x, y) for x in [1, 2, 3] for y in [3, 2, 1] if x != y]
print(product)

# order is important (symbol does not exist) or different order of tuples
#product = [(x, y) for x in [1, 2, 3]  if x != y for y in [3, 2, 1]]
#print(product)

# Compare this to the actual loop version (and how much more expressive Python is here)
product = []
for x in [1, 2, 3] :
    for y in [3, 2, 1] :
        if x != y :
            product.append((x, y))
print(product)

# list comprehensions can be nested (its the expression of another list comprehension)
# Lets take a matrix (2-dimentional array)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# The transpose of this is (flip rows/columns):
transpose = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]

# With a list comprehension
# first lest iterate over every row
transpose = [row for row in matrix]
print(transpose)

# This may be a bit difficult, but
# now we got every row and we want to generate the transpose
# So, for transpose we need the first position from each row
# second, we need second position, etc.
# What does that sound like?
# For value 0 (outer), we go through each row of matrix and generate a new row (inner)
# Continue for 1, and 2
transpose = [[row[i] for row in matrix] for i in range(3)]
print(transpose)

# This is some hard to wrap your head around stuff, but
# can you help me try and square all elements in an matrix?
# So, we are generating a 2-D array (so, nested list comprehension)
square = [[element ** 2 for element in row] for row in matrix]

# del - deletes items from list and variables
a = 42
print(a)
del a
#print(a)

# How do you delete an element in an array
data = [1, 2, 3]
data[1:2] = []
print(data)

# can also use del
data = [1, 2, 3]
del data[1]
print(data)

# can also be used for more sequence types


# Tuple packing and unpacking
# Extension to what we saw earlier

# pack
tuple = 0, 1
print(tuple)

# unpack
prev, current = tuple
print(prev, current)

# How do we create dictionaries?
dictionary = {'key': 'value'}
print(dictionary)
#or
dictionary = dict([('key', 'value')])
print(dictionary)

# if key are strings, can
dictionary = dict(jack=4139, jill=4127, hill=4098)
print(dictionary)

# You can bind multiple values in for
for index, value in enumerate(['eeny', 'mini', 'miny', 'moe']) :
    print(index, value)


# Dict looping
questions = {'name': 'lancelot', 'quest': 'the holy grail', 'favorite color': 'blue'}
for key, value in questions.items() :
    # format a string
    'What is your {0}?  It is {1}.'.format(key, value)
    print('What is your {0}?  It is {1}.'.format(key, value))



# So, if you drop the ':' syntax, you get a set
# basically a dictionary where the key is also the value
a_set = {'item'}
print(a_set)

# sets do not allow duplicates
set_one = set('kadabra')
print(set_one)
set_two = set('alakazam')
print(set_two)

# What operations are there on a set : union, intersection, difference
# difference
print(set_one - set_two)

# intersection
print(set_one & set_two)

# union
print(set_one | set_two)

# symmetric difference
print((set_one - set_two) | (set_two - set_one)) # and other ways
print(set_one ^ set_two)

# set and dictionary comprehensions also exist and use {}
a_set = {x for x in 'kadabra' if x not in 'abk'}
print(a_set)

# Sequences (same type) can be compared (lexographically (iterative apply comparison to elements))
print([1, 2, 3] == [1, 2, 3])
print([1, 2, 3] < [1, 2, 4])

