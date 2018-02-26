##
# @file exceptions.py
#
# Modules and packages in Python based on: https://docs.python.org/3/tutorial
#
# @author Michael John Decker, Ph.D.
#

# python namespace is a mapping from names to objects
# E.g.,builtin namespace (interpretter startup), global namespace (created when read in), function local namespace (on call)
# declarations in a namespace are attributes (. operator)

done = False
while not done :
    try :
        x = int(input('Enter a number: '))
        # skipped on exception
        done = True

    # if exception matches
    #except ValueError:
    # if not correct exception type (decendent of Exception class)
    #except str :
    #except ArithmeticError :
    # You can have multiple values in an except
    #except (ValueError, ArithmeticError) :
    # except everything (must be last)
    except :
        print('Not a number. Please, try again.')
        # reraise
        raise
    # except ValueError:
    #     pass


# You can also have multiple except

class error(Exception):
    pass
class fatal(error) :
    pass
class warning(error):
    pass

# a list of types!!!
for aclass in [error, fatal, warning] :

    try :
        # raise exception
        raise aclass()

    # first matching is executed (put error first) and try
    # except error :
    #     print('An error occurred')
    # except fatal :
    #     print('A fatal error occurred')
    # except warning :
    #     print('A warning occurred')


    except fatal :
        print('A fatal error occurred')
    except warning :
        print('A warning occurred')
    except error :
        print('An error occurred')


import sys
for arg in sys.argv[1:] :
    try :
        file = open(arg, 'r')
    except OSError :
        print('cannot open', arg)
    # on success of all of try (must be after all except)
    else :
        print(arg, ':', len(file.readlines()), 'lines')
        file.close()


# Instance variable can be accessed
try :
    # cause exception to occur (instance (default ctor) or class)
    raise Exception('one fish', 'two fish', 'red fish', 'blue fish')
except Exception as exception:
    print(type(exception))
    # the args as tuple
    print(exception.args)
    # via __str__
    print(exception)

    cat, i_n, the, hat = exception.args
    print('arg1:', cat, 'arg2', i_n, 'arg3:', the, 'arg4:',hat)
    # args are printed when unhandled
    #raise

# finally is always run (cleanup), Java has this too
def divide(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

divide(0, 1)
print()
divide(1, 0)
print()
# runs finally before breaks (finally very useful for files/network connections)
divide('2', '1')
