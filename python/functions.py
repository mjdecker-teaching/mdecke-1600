##
# @file functions.py
#
# functions statements in Python based on: https://docs.python.org/3/tutorial
#
# @author Michael John Decker, Ph.D.
#

# Were switching to an editor instead of REPL.

# A function is born when you use the def reserved word
def hello() :
    print('Hello')

# function needs declared before it is called at runtime
hello()

n = 0
def foo():
    print('foo')
    # Won't work
    #n += 1
    globals()['n'] += 1
    if n < 3 :
        bar()

def bar():
    print('bar')
    foo()

foo()

# This redefines the function with a parameter 
def hello(name) :
    print('Hello', name)
# old function is gone
#hello()
hello('Michael')

# The execution of a function introduces a new symbol table 
# used for the local variables of the function. More precisely, 
# all variable assignments in a function store the value in the 
# local symbol table; whereas variable references first look in 
# the local symbol table, then in the local symbol tables of enclosing
# functions, then in the global symbol table, and finally in the table
# of built-in names. Thus, global variables cannot be directly assigned
# a value within a function (unless named in a global statement),
# although they may be referenced.

# The actual parameters (arguments) to a function call are
# introduced in the local symbol table of the called function
# when it is called; thus, arguments are passed using call by value
# (where the value is always an *object reference*, not the value
# of the object). When a function calls another function, a new 
# local symbol table is created for that call.

def fibonacci(max_num) : 
    """Print Fibonacci numbers up to max_num""" # docstring
    prev, current = 0, 1
    while prev < max_num :
        print(prev, end=' ')
        prev, current = current, prev + current
    print()

fibonacci(2000)

# function definition introduces a new name
print(fibonacci)
print(fibonacci.__doc__)
# Python supports aliasing
fibo = fibonacci
fibo(2000)

def fibonacci_list(max_num) :
    """Returns an array with the Fibonacci numbers up to max_num"""
    prev, current = 0, 1
    fibo_list = []
    while prev < max_num :
        fibo_list.append(prev)
        prev, current = current, prev + current
    return fibo_list

print(fibonacci_list(2000))

# All functions actually return something
print(fibonacci(2000))

# multiple return
def next_fibo(prev, current) :
    return current, prev + current

a = next_fibo(0, 1)
# a is what is called a tuple (math def = finite ordered list (sequence))
# basically an immutable list
print(a)

# can be unpacked
a, b = next_fibo(0, 1)

# Parameters

# Default parameters
def guessing_game(values, answer_pos = 0, tries_param=3) : 
    if answer_pos < 0 or answer_pos >= len(values) :
        print('Invalid answer position')
        return

    tries = tries_param
    for atry in range(tries) :
        print(tries, 'tries remaining')
        # Can cast to string
        guess = input('Guess from one of the following: ' + str(values) + ' ')

        # in tests membership
        if guess not in values :
            print('Invalid guess')
        elif values[answer_pos] == guess :
            print('Good, good, but you are not a Jedi, yet')
            break
        tries -= 1
    else :
        print('You failed')

# ask students for participation on values
#guessing_game(['a', 'b', 'c'])

# one or both default params can be specified
#guessing_game(['a', 'b', 'c'], 2)
#guessing_game(['a', 'b', 'c'], 2, 5)

# default values are evaluated at defining scope
i = 5
def i_func(val=i):
    print(i)
i = 42
i_func()

# WARNING WARNING WARNING
# default parameters are assigned to only once
# It is good practice (any language) to not modify parameters used only for reading
def list_append(value, alist = []) :
    alist.append(value)
    return alist

print(list_append(0))
print(list_append(1))
print(list_append(2))

# Keyword arguments
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

# parrot()                     # required argument missing
# parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
# parrot(110, voltage=220)     # duplicate value for the same argument
# parrot(actor='John Cleese')  # unknown keyword argument

# keyword arguments must exist and follow positional, but order of keyword do not matter
# No argument can be assigned to twice

# keyoword arguments can also appear after *name
def donut_shop(kind, *arguments, **keywords) :
    print('Do you have any', kind, 'donuts?')
    print('Naaah, we are out of', kind, 'donuts.')

    # additional positional populate *name
    for argument in arguments :
        print(argument)

    # additional keyword populate **name
    for keyword in keywords :
        print(keyword, ':', keywords[keyword])

# order of both is maintained
donut_shop('glazed', 
           'Well, in that case. In that case. What do you have?',
           'All I\'ve got right now is this box of one dozen starving crazed weasels.',
           artist='Wierd Al',
           song='Albuquerque')

# brief dictionary
# empty dictionary
birthday_dict = {}
# key value pairs, key index to value
birthday_dict['Decker'] = 'September 7th'
birthday_dict['Reese'] = 'February 15th'
birthday_dict['Decker']

# or specify one go
birthday_dict = { 'Decker': 'September 7th', 'Reese': 'February 15th'}


# unpacking
params = [3, 6]
range(*params)

params = {'voltage': 'four million', 'state': 'bleedin\' demised', 'action': 'VOOM'}
parrot(**params)

# Show them annotations: https://docs.python.org/3/tutorial/controlflow.html#defining-functions

# Have them read 4.7.6. Documentation Strings and 4.8: https://docs.python.org/3/tutorial/controlflow.html#defining-functions


