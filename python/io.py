##
# @file io.py
#
# IO in Python based on: https://docs.python.org/3/tutorial
#
# @author Michael John Decker, Ph.D.
#

# str vs repr
lyric = "If you don't eat your meat, you can't have any pudding!"

# human readable
print(str(lyric))
# interpreter readable
print(repr(lyric))


# format via string.format
import math
print('PI: {0:.5f}, Gravity: {1:2d} ft/sec'.format(math.pi,  32))

# There are a course a lot more ways to use format...

# file io
# could not be much easier...

# file = open(filename, mode)
# r is read, w is write, r+ is rw, b is byte, a is append
file = open('dijkstra.txt', 'r')

quote = file.read()
#quote = file.read(size)
#quote = file.readline()
#liens = file.read().splitlines()

# if you open, you must close
file.close()

print(quote)

infile = open('dijkstra.txt', 'r')
outfile = open('stripped.txt', 'w')

for line in infile:
    #print(line)
    outfile.write(line.strip())

infile.close()
outfile.close()
# look at file output


# with-statement -auto closes
with open('dijkstra.txt') as dijkstra_file :
        data = dijkstra_file.read()
print(dijkstra_file.closed)

# Python also support json input/output, and my favorite pickle: https://docs.python.org/3/library/pickle.html#module-pickle
