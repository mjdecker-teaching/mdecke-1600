##
# @file while.py
#
# While-statement in Python based on: https://docs.python.org/3/tutorial
#
# @author Michael John Decker, Ph.D.
#

#while condition :
#    (tabbed) statements

# condition: C style boolean operators
# tabbed: space is significant.  
# * Avoid mixing tabs and spaces, Python relies on correct position
#   and mixing may leave things that look indented correctly, but are not
# * http://www.emacswiki.org/emacs/TabsAreEvil
#

# How might you compute fibonacci (while number is less than 10)?

last = 0
current = 1
while last < 10 :
    print(last)
    temp = current
    current = last + current
    last = temp

# Python improvement 1) multiple assignment
# first is in C++, other is not
last, current = 0, 1
while last < 10 :
    # need to indent
    print(last)
    # no temp!!!  All, rhs is evaluated before any actual assignment
    last, current = current, last + current

# conditions
# * boolean: True, False
while True :
    print('Do not do this: ^C to stop')
while False :
    print('Never executed')

# * integer: 0 False, True otherwise
count = 10;
while count : 
    print(count)
    count -= 1

# * sequence: len() == 0 False, True otherwise
sequence = ['bar', 'foo']
while sequence :
    print(sequence[-1])
    tos = sequence.pop()


# Python supports usually comparisons and 
# 'and', 'or' and 'not'(C++ has these, but have different precedence)
# https://docs.python.org/3/library/stdtypes.html
# notice that ! is not suppported.  Python 2 had <> as well (!=)
# conditions can be chained (but are ands)
x = 1
y = 2
z = 3
x < y <= z

# print is a bit ugly...

# Here is simple print usage:  Multiple arguments are handled
# They are space separated, no quotes for strings, and ending in a newline
print("256 ** 2:", 256 ** 2)

last, current = 0, 1
while last < 10 :
    # We can specifiy the end character (this is a keyword argument, more when we see functions)
    print(last, end=',')
    last, current = current, last + current
