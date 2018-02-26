##
# @file coroutines.py
#
# Coroutines in Python based on: https://docs.python.org/3/tutorial
#
# @author Michael John Decker, Ph.D.
#

# Coroutines is a more general generator (specify courouting to jump to)
# https://en.wikipedia.org/wiki/Coroutine
# Similar to mutual recursion with tail recursion (no new stack frame), but more flexible/effidient
# (do not restart (resume), yield instead of return (which has to be in tail),
# hold state)

# Reuse circular queue
class circular_queue : 

    def __init__(self, max_size = 128) :
        self.max_size = max_size
        self.queue = [None] * self.max_size
        self.size = 0
        self.start = 0
        self.end = -1

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

    def __str__(self) :
        return 'size: {0} queue: {1}'.format(self.size, str(self.queue))

    def __iter__(self) :
        return circular_queue_iterator(self)

    def generate(self) :
        for i in range(self.size) :
            yield self.queue[(self.start + i) % self.max_size]

done = False
queue = circular_queue(4)
def produce() :
    print('Enter produce')

    while not done : 
        while not queue.is_full() :
            queue.enqueue(input('Item: '))
        yield consume
    print('Exit produce')

def consume() :
    print('Enter consume')

    while not done :
        while not queue.is_empty() :
            print(queue.dequeue(), end = ', ')
        print()
        yield produce

count = 5
routines = { produce: produce(), consume: consume() }
current = produce
while not done :
    count -= 1
    if count == 0 : done = True
    try : 
        current = next(routines[current])
    except StopIteration :
        pass

# To use with-statement, define __enter__ and __exit__
class resource : 

    def __init__(self, filename) :
        print('Constructor')
        self.file = open(filename, 'r')

    def __enter__(self) :
        print('enter')
        return self

    # if no exception was raised, arguments are None
    def __exit__(self, exc_type, exc_value, traceback) :
        print('Exit')

        # True, means do not propagate exception
        return True


obj = resource('dijkstra.txt')
print('pre with-statement')
with obj as rsrc :
    print('with-statement')

