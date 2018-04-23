##
# @file lists.py
#
# Lists in Python based on: https://docs.python.org/3/tutorial
#
# @author Michael John Decker, Ph.D.
#
#

# So what do you think a list is:
# an array
fibonacci = [0, 1, 1, 2, 3]
fibonacci

# lists are another sequence type like strings and 
fibonacci[0]
fibonacci[-1]
fibonacci[-3:]

# Tell me about C++ arrays, such as what restrictions?
# They are homogeneous...
# Python are not restricted to same element, but often are...
record = ['Final Fantasy Brave Exvius', 'gumi, Inc.', 2016]
record[0]
record[1]
record[2]

# concatenation is supported
fibonacci + [5, 8, 13, 21, 34]
# original is unmodified
fibonacci

# Multiplication is supported
doubled = fibonacci * 2
fibonacci
doubled

# So, strings are immutable, what about lists?
cubes = [1, 8, 27, 65, 125]
# 65 is not right
4 ** 3
# fix
cubes[3] = 64
cubes

# Well, concatenation creates a new list, which can be very inefficient, appending?
cubes.append(216)
cubes.append(7 ** 3)
cubes

# But, I have a list I need added...
fibonacci.extend([5, 8, 13, 21, 34])
fibonacci

# Modification with slices?
grades = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
grades

# replace
grades[2:5] = ['C', 'D', 'E']
grades

# They need not be the same size
grades[3:7] = ['d', 'f']
grades

# or erase
grades[1:4] = []
grades


# lists are not copied on assignment
original = [1, 2, 3]
copy = original
copy[2] = 5
original

# new list
copy = [3, 2, 1]
copy
original

# shallow copy (lists are but not contents)
copy_fib = fibonacci[:]
copy_fib[0] = 42;
fibonacci
copy_fib

# Like string, len gives the length
len(grades)

# Lists can contain lists
song_one = ['Jonathan Coulton', 'Code Monkey', 2006]
song_two = ['Basshunter', 'DotA']

songs = [song_one, song_two]
songs
