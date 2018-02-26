##
# @file classes.py
#
# Modules and packages in Python based on: https://docs.python.org/3/tutorial
#
# @author Michael John Decker, Ph.D.
#

# python namespace is a mapping from names to objects
# E.g.,builtin namespace (interpretter startup), global namespace (created when read in), function local namespace (on call)
# declarations in a namespace are attributes (. operator)
import sys

# behaves as object
print(sys)
sys.stderr

# What are the python scopes again?
# innermost (local) scope, enclosing functions, globals, built-ins
# scoped are static, but name resolution is dynamic (this is possibly changing)
# assignment and del add and remove bindings (that word again) and go to local scope
# import and function decl bind names in local scope

# Scoping example
def python_scope() :
    def local_scope() :
        scam = 'local scam'

    def nonlocal_scope() :
        # non local will continue up functions until first found variable
        nonlocal scam
        scam = "nonlocal scam"

    def global_scope() :
        # no previous binding
        global scam
        scam = 'global scam'

    scam = 'python scam'
    print('local scope:', scam)

    local_scope()
    print('local assignment:', scam)

    nonlocal_scope()
    print('nonlocal assignment:', scam)

    global_scope()
    print('global assignment:', scam)

python_scope()
print('global scope:', scam)


# Based off of C++ and Modula-3
# Allows: inheritance, multiple base classes, override methods, call base class methods

# like functions must be executed (encountered before use)
class bird :
    pass

# class definitions create a new namespace and local scope

# Like function, and othe things in python classes are objects
print(bird)

# Classes can be modified at runtime
# All normal members are public and all methods virtual
# builtins can be base class
# operators can be overloaded

# objects are aliased when assigned (or passed, another way to think about the pass by object-reference)
larry = bird
print(larry)

# A simple class
class bird :
        """A bird class"""
        type = 'Swallow'

        def velocity() :
            return 11

# calling object (instantiation)
swallow = bird()

print(bird.type)
print(bird.velocity())


# constructor
class bird :

    # first argument is always the object (like this in C++)
    # self is convention (some editors (like Sublime)) rely on it
    # strongly urge following this convention
    def __init__(self, type, airspeed = 11) :
        # added at runtime
        self.type = type
        self.airspeed = airspeed

    def velocity(self) :
        return self.airspeed



# Class instances (no classes themselves) have two type of attributes: data and methods
# data (data members)
european = bird('European Swallow')
print(european.type)

european.carrying_coconut = True
print(european.carrying_coconut)
del european.carrying_coconut

# never happened
# methods
print(bird.velocity)
print(european.velocity)

assert bird.velocity(european) == european.velocity()

# a method object is created on refence
european_velocity = european.velocity

print(european_velocity)
print(european_velocity())
# methods have some attributes
print(european_velocity.__self__)
print(european_velocity.__func__)

class cat :

    # class variable (shared)
    kind = 'feline'

    # incorect usage of variable
    tricks = []

    def __init__(self, name) :
        # instance variable
        self.name = name

    def add_trick(self, trick) :
        self.tricks.append(trick)


# ask for cat names
c = cat('Shampoo')
d = cat('Spot')

c.add_trick('sleep')
d.add_trick('scratch')

print(c.tricks)

# Remarks
# data attributes override method attributes with same name
# Python does not support data hiding (convention does)
# Class functions need not be declared in a class

# Inheritence (Base name may be module.classname)
# Scoping: If attribute not resolved in class, searches base class (applied recursively)
class european(bird) :
    def __init__(self) :
        self.type = 'European Swallow'
        self.airspeed = 11

class african(bird) :

    load_factor = 2

    def __init__(self, number_coconuts) :
        self.type = 'African Swallow'
        self.airspeed = 42
        self.number_coconuts = number_coconuts

    def velocity(self) :
        #return self.airspeed - self.number_coconuts * african.load_factor
        return bird.velocity(self) - self.number_coconuts * african.load_factor
        return super().velocity() - self.number_coconuts * african.load_factor


def print_bird(birdie) :
    print('type:', birdie.type, 'velocity:', birdie.velocity())


# is this polymorhpism?
e = european()
print_bird(e)
a = african(1)
print_bird(a)

# builtin inheritence functions (may also have tuple of types)
print(isinstance(e, bird))
print(isinstance(e, european))
print(isinstance(e, (bird, european)))
print(isinstance(e, african))
print(isinstance(e, (bird, african)))

print(issubclass(bool, int))
print(issubclass(bool, bird))


# multiple inheritence
# attributes inherited from a parent class as depth-first, left-to-right, not searching twice in the same class where there is an overlap in the hierarchy
# all inherit indirectly from objec if not specified
class norwegian_blue(bird, object) :
    pass

# no private, but leading underscore is convention for private
# if two leading underscore and at most one trailing name will be name mangled (avoid collision in super/sub classes)
# https://en.wikipedia.org/wiki/Name_mangling#Python

# Special methods (e.g., operator overloading)
# https://docs.python.org/3/reference/datamodel.html
# Operator overloading alone is why Python > Java

class point :
    def __init__(self, x, y) :
             self.x = x
             self.y = y

    def __add__(self, other) :
        return point(self.x + other.x, self.y + other.y)

    # try with and without __str__
    def __str__(self) :
        return str((self.x, self.y))

point_one = point(1,2)
point_two = point(3,4)

print(point_one + point_two)

