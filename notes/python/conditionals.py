##
# @file conditionals.py
#
# Conditional statements in Python based on: https://docs.python.org/3/tutorial
#
# @author Michael John Decker, Ph.D.
#

# if-statement

# What do you think an if is like in Python?
num = 0
if num < 0 : 
    print('negative')

# Ofcourse we have an else
num = 0
if num < 0 : 
    print('negative')
else :
    print('non-negative')

# What about nested chains?
# num = 0
# if num < 0 : 
#     print('negative')
# else if num == 0 : # not valid
#     print('zero')
# else :
#     print('positive')

num = 0
if num < 0 : 
    print('negative')
elif num == 0 :
    print('zero')
else :
    print('positive')


# You can have multiple elif (substitute for switch/case)
num = 2
if num < 0 : 
    print('negative')
elif num == 0 :
    print('zero')
elif num == 1 :
    print('one')
else :
    print('more')

# To make things easier lets mess with input: try with 1 and foo

num = input('Please input an integer: ')
# A bit disceptive, its a string (no ending newline) 
print(num)
num

# need to convert to int, has function style casting: try with 1 and foo
num = int(input('Please input an integer: '))

# There are occasions when input from terminal is usefull (password), however, generally want process automated

# Someone asked about infinite making of nested lists
# bad_list = []
# while True :
#     new_list = []
#     new_list.append(bad_list)
#     bad_list = new_list


# for-statements
# What forms of for statements you have in C++?
# for(int i = 0; i < 10; ++i); and for(int i : array); 
# Python's for is like the range-based for it iterates over items in a sequence (in order)

animals = ['cat', 'dog', 'fish', 'echidna']
for animal in animals :
    print(animal, len(animal))

# What if you modify the list in the loop
animals = ['cat', 'dog', 'fish', 'echidna']
for animal in animals :
    animals.insert(0, animals[3]) 
    print(animals)


# Can iterate over a copy
animals = ['cat', 'dog', 'fish', 'echidna']
for animal in animals[:] :
    animals.insert(0, animals[3])
print(animals)

# But what if you need a sequence of numbers?
# Never, fear the range is here?
for i in range(5) :
    # sequence 0, 1, 2, 3, 4 (think mimic i < 5)
    # stop is never included
    print(i, end=' ')

# range(stop)
# range(start, stop[, step])
for i in range(5, 10) : print(i, end=' ')
for i in range(0, 10, 3) : print(i, end=' ')
for i in range(-10, -100, -30) : print(i, end=' ')

# Given what you know of lists/strings and range,
# How do you iterate over the indices of this list to print (index, vegetable)?
vegetables = ['carrot', 'radish', 'napa cabbage']
for index in range(len(vegetables)) :
    print(index, vegetables[index])

# see a bit more why end point not included in range?
# Could also use enumerate, but we have not done tuples, yet

# Some scoping we will talk more later
# What in C++ is in an not in scope, Python?
for i in range(5) :
    # sequence 0, 1, 2, 3, 4 (think mimic i < 5)
    print(i, end=' ')

print(i)

integer = 0
while integer < 10 :
    integer += 1
    sum = integer

print(integer, sum)

# https://docs.python.org/3/library/stdtypes.html#range
# Actually, an immutable sequence type (object) that returns the successive items
# when you iterate over it.  No, list need generated.
print(range(10))

# However, can be converted to a list with function style cast
# Like most types in Python
list(range(10))

# There are more iterable items in Python for the various types

# break, continue, and loop-else?
# First, break
# lets search for what is divisible by what
for n in range(2, 10) :
    for x in range(2, n) :
        if n % x == 0 :
            print(n, 'equals', x, '*', n//x)
            break

# What if we want to know if it is a prime, what might we do?
# Various answers, another loop, extend n to plus 1, and check if reach
# Now something you have never seen
for n in range(2, 10) :
    for x in range(2, n) :
        if n % x == 0 :
            print(n, 'equals', x, '*', n//x)
            break
    # eyes are not decieving you (the else goes with the for)
    else :
        # loop fell through without finding a factor (executed if list exhausted)
        print(n, 'is a prime number')


# While also has an else which executes when it is False
# Actually, both are sort of when false
i = 0
while i < 21 : 
    print("2 ** ", i, ' = ', 2 ** i)
    i += 1
else :
    print ("21 = blackjack")

# continue is also supported
occupations = ['policeman', 'scientist', 'waldo', 'president']
for occupation in occupations : 
    # guard clause - a precondition check to protet and simplify main execution branch
    # deviation of structured programming
    if occupation != 'waldo' :
        continue
    print('Found Waldo!!!')

# pass is basiclly a noop statement.  Fills blocks with nothing
while True :
    pass
