##
# @file modules.py
#
# Modules and packages in Python based on: https://docs.python.org/3/tutorial
#
# @author Michael John Decker, Ph.D.
#


# A module is a file containing Python definitions statements
# The name is the file minus the .py
import function

# first the set of built-in modules is searched then variables in sys.path are searched
# you can also modify at runtime
import sys
print(sys.path)

# definitions are namespaced with the module name
print(function.binary_search([1, 2, 3, 4], 3, 0))

# you can ask the module's  name
print(function.__name__)

# Remember you can alias in Python
#binary_search = function.binary_search
#print(binary_search([1, 2, 3, 4], 3, 0))


# You can also directly import a name
from function import binary_search
from function import insertion_sort, split_char
print(binary_search([1, 2, 3, 4], 3, 0))

# can also important anything not beginning with _
# not recommended same as using namespace std;
from function import *

# When you run a program from the command line it gets the __main__ namespace
print(__name__)

# you can use this to run statements when run (and not imported)
if __name__ == "__main__" :
    # do main processing
    import sys
    # process command line
    print(sys.argv[0])



# Compiled Python - __pycache__/module.version.pyc

# Packages
# show package directory
#import package
#import package.submodule

# Use __all__ to for * syntax
# bar still not initialized
from package import * 