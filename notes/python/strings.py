##
# @file strings.py
#
# strings in Python based on: https://docs.python.org/3/tutorial
#
# @author Michael John Decker, Ph.D.
#

# What type do you thing this is?
"butterscotch"

# How about this one?
'a'

# Both are strings
'butterscotch'

# Just as in C++, \ can be used to escape characters
'\'escaped\''

# Or use the other type of quote
"'no need to escape these'"
'"or these"'

# print, how real output is done, Python 2 requires no parenthesis (might be why people still use 2)
'"It\'s just a flesh wound." Black Knight'
print('"It\'s just a flesh wound." Black Knight')

# How do you think you print a '\'?
# escape 
print('C:\\WINDOWS\\system32')

# raw strings
print(r'C:\WINDOWS\system32')

# What you always wanted, multi-line quotes.

"""This was a triump
I'm making a note here
HUGE SUCCESS
"""

# Can use either quote, no need to escape
'''It's hard to overstate
my satisfaction
Aperture Science
'''

# If you want to suppress new line being appended use \ (line continuation character?)
'''\
program arg [optional_arg]
  * arg - an argument
  * optional_arg - an optional argument\
'''

# concatenation
"Fat Man" + " and " + "Little Boy"

# string multiplication
"ha" * 3 + " " + "ha" * 7

# string next to each other are concatenated automatically
'Muffin ' 'Button'

# to break into long lines use parenthesis
# What type is this?
text = ('Your mother was a hamster and '
        'your father smelt of elderberries!')
text

# must both be literals, not variables or expressions
prefix = 'Py'
#prefix 'thon'
#('un' * 3) 'ium'

prefix + 'thon'

# [] operator supported (well, arrays in general support these ops)
bird = 'word'
bird[0] # 0-position offset
bird[3]
bird[3][0] # these are strings of size 1

# bird[4] - errors 

# negative numbers?
bird[-1] # negative offset cause -0 == 0
bird[-4]

# bird[-5] - error

# slicing in this case substring, but applies to other lists
word = 'Python'
word[0:2] # left included, right excluded [0,2)
word[2:5] # length is 5 - 2 == 3

# empty sides expand to remaining part of list (front or back)
word[:2]
word[2:]

# note, the indexing is on purpose so
word[:2] + word[2:] 
word[:3] + word[3:] 

# negatives with slicing?
# what you think we get
word[-2:]

# Way to think about it, numbers are the boundaries, take everything in between
#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1
word[-4:-1]

# out of bounds on slice? Gracefully handled.
word[4:42]
word[42:]

# strings are immutable!
#word[0] = 'C'
#word[2:] = 'py'

# have to create a new one
'C' + word[1:]
word[:2] + 'py'

# immutability.  Some things in Python provide both a mutable (bytearray) and immutable version.  Immutable has usage, for example, for hasing (a topic for latter)

# length (also for lists)
long_word = 'antidisestablishmentarianism'
len(long_word)

# unicode (python 2 is not unicode by default)
greek = 'αβγ'
