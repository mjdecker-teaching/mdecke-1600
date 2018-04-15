##
# @file basics.py
#
# Basic Python programming based on: https://docs.python.org/3/tutorial
#
# @author Michael John Decker, Ph.D.
#
#
# General Information
# * High-level programming language
# * General-purpose (vs. domain specific)
# * Created by Guido van Rossum (1991)
# * Emphasizes: 
#     * Code readability
#     * Highly-expressive syntax
#
#
# Some specifics
# * Intepreted
# * Dynamically typed (with duck typing)
# * Strongly typed
# * Paradigms (includes)
#    * imperative
#    * procedural
#    * object-oriented
#    * functional
# * Whitespace is significant (no blocks, i.e, {} )
#
# Website: https://www.python.org
#
# Downloads: # * https://www.python.org/downloads/
# * Python 3 (similar, but not compatible with Python 2)
#   * Windows - Use installer
#     * set path=%path%;C:\python36
#   * Mac - should use Homebrew, or website
#   * Unix - package manager, or website  
#     * export PATH="PYTHON_INSTALL_DIRECTORY:$PATH"
#     * Never put '.' (current directory) in path.
#
#  
# Language Info: https://docs.python.org/3/
# or just google
#
# Tutorial: https://docs.python.org/3/tutorial/appetite.html
# * Show, line where it is named afer Monty python
# * For fun, http://legacy.python.org/search/hypermail/python-1994q2/0003.html
#
# also this
import antigravity
#
# python3
# * read–eval–print loop (REPL)
# python3 program.py [args] (how to access in program at later date)
# * Execute python program
#
# Unix
# * At top of file, '#!/usr/local/bin/python3' and make file executable (UNIX "shebang" line)
# Python Tool doc - (https://docs.python.org/3/using/cmdline.html#using-on-general)
# * Or, man python3 (unix)
#
# Interactive Mode:
# * >>> usually primary prompt
# * ... secondary prommpt (e.g., multiple line constructs)
# * nothing is output
# * Unix ^ + D, Windows ^ + Z, exit(), or quit()
#    * ^ is control
#
# Python Encoding
# * Put '# -*- coding: encoding -*-' as first line of a file
# * May occur after shebang line

# In REPL:

# What... is the airspeed of an unladen swallow?
airspeed_velocity = 11  # What do you mean? An African or European swallow?
          # Huh? I... I don't know that. Auuuuuuuugh.
text = "# Three above are quotes, This is not as it's inside quotes."

# Python as a simple calculator
2 + 2

# Order of ops: https://docs.python.org/3/reference/expressions.html#operator-precedence
42 - 5 * 6

# Typical force precedence (4.0 - to set up next one)
(42 - 5 * 6) / 4.0

# What do you think we get, nope, a float (differs from Python2)
8 / 5

# Now, an int (floor function)
8 // 5

# Python 3: has only one integer number and floating-point number type (long in python 2, but int in python was a C long?, but unlimited precision) and float (usually a double)

# modulus
8 % 5

# powers
2 ** 10

# as this is a programming language that can change state we have assignment
# An identifier can is [:alpha:_][:alphanum:_]* unlimited length and case significant.
# Python 3 adds unicode
Δ = 4 - 3

# what type of type systems is this, again?
base = 10
power = 3
# if do not remember precedence use ()
base ** power * 9 + 1

# Can mix int and float types (What do you think about this: strong or weak typing?)
32 * .25 - 1

# In REPL, result of last printed expression is held in _
tax = 6.75 / 100 # variable has what type now?
price = 8 + 12 # variable has what type now?
price * tax
price + _
round(_, 2)

# treat _ as read-only, as creates a new variable hiding built-in variable with its magic behavior (Python's words BTW)
_ = 42
7 * 3
_

# Python additionally suport: complex numbers, Decimal, and Fraction
