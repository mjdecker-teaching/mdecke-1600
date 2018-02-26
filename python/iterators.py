##
# @file iterators.py
#
# Modules and packages in Python based on: https://docs.python.org/3/tutorial
#
# @author Michael John Decker, Ph.D.
#

# python namespace is a mapping from names to objects
# E.g.,builtin namespace (interpretter startup), global namespace (created when read in), function local namespace (on call)
# declarations in a namespace are attributes (. operator)
import functools

@functools.total_ordering
class circular_queue : 

    class iterator :

        def __init__(self, circular_queue) :
            self.circular_queue = circular_queue
            self.count = 0

        def __next__(self) :
            if self.count == self.circular_queue.size :
                raise StopIteration

            self.count += 1
            return self.circular_queue.queue[(self.circular_queue.start + self.count - 1) % self.circular_queue.max_size]

    # start with this much completed and explain (unless do not know what one is)
    def __init__(self, max_size, iterable = []) :
        assert max_size > 0
        self.max_size = max_size
        self.queue = [None] * self.max_size
        self.size = 0
        self.start = 0
        self.end = -1

        for i in iterable : self.enqueue(i)

    def enqueue(self, item) :
        assert not self.is_full()
        self.size += 1
        self.end = (self.end + 1) % self.max_size
        self.queue[self.end] = item

    def dequeue(self) :
        assert not self.is_empty()
        item = self.front()
        self.size -= 1
        self.start = (self.start + 1) % self.max_size
        return item

    def front(self) :
        assert not self.is_empty()
        return self.queue[self.start]

    def back(self) :
        assert not self.is_empty()
        return self.queue[self.end]

    def is_full(self) :
        return self.size == self.max_size

    def is_empty(self) :
        return self.size == 0

    def __repr__(self) :
        return str(self.queue)

    # new stuff here
    def __iter__(self) :
        return circular_queue.iterator(self)

    def __str__(self) :
        return 'size: {0} queue: {1}'.format(self.size, str(list(self)))

    # not really a good name, but to differentiate between iterator
    # generators (use of yield) auto implements the __iter__() and __next__() (with StopIteration)
    # local variables and execution state are also saved between calls
    # so this actually works as expected
    def generate(self) :
        for i in range(self.size) :
            yield self.queue[(self.start + i) % self.max_size]



    # in-class

    # reverse using generator
    def __reversed__(self) :
        for i in reversed(range(self.size)) :
            yield self.queue[(self.start + i) % self.max_size]


    def __contains__(self, item) :
        for i in self :
            if i == item :
                return True

        return False


    # equality (currently held elements)
    def __eq__(self, other) : 
        assert isinstance(other, circular_queue)
        return list(self) == list(other)

        # if self.size != other.size : return False
        # for i in range(self.size) :
        #     if self.queue[(self.start + i) % self.max_size] != other.queue[(other.start + i) % other.max_size] :
        #         return False
        # return True


    # less then (currently held elements) (after shown equality)
    def __lt__(self, other) :
        assert isinstance(other, circular_queue)
        return list(self) < list(other)


# generators
queue = circular_queue(3)
#queue.dequeue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(repr(queue))

# queue.enqueue(4)
queue.dequeue()
queue.dequeue()
queue.enqueue(4)
queue.enqueue(5)
print(repr(queue))

queue.dequeue()
queue.dequeue()
queue.enqueue(6)
queue.enqueue(7)
print(repr(queue))


# iterators (if outside)
class circular_queue_iterator :

    # can be other object (may want multiple ways to iterate over) or
    # self can be returned if the container itself implement __next__()

    def __init__(self, circular_queue) :
        self.circular_queue = circular_queue
        # use it to track where we are currently
        self.count = 0

    def __next__(self) :
        if self.count == self.circular_queue.size :
            raise StopIteration

        self.count += 1
        return self.circular_queue.queue[(self.circular_queue.start + self.count - 1) % self.circular_queue.max_size]

# iterators
# So, we mentioned for works with all containers
# The way this works is that the for calls iter() (builtin) on the container.
# iter() returns an iterator object which defines __next__()

string = 'otter'
# calls __iter__()
itr = iter(string)
# next() is builtin version calls __next__()
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
# calls StopIteration
# print(next(itr))
print()

for i in queue :
    print(i)
print()

# generators
for i in queue.generate() :
    print(i)


print(queue)

# generator expressions
print((i for i in range(3)))
listified = list(i for i in queue)
print(listified)
