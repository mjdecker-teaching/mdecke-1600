## 
# @file linked_list.py
#
# Template for linked_list class.
#
# @author Michael John Decker, Ph.D.

class node :
    def __init__(self, item, prev = None, next = None) : 
        self.item = item
        self.prev = prev
        self.next = next

    def __str__(self) :
        return str(self.item)

    def __repr__(self) :
        return repr(self.item)


## linked_list
# Implements a doubly-linked list ADT
# @invariant (len == 0 and head == None and tail == None)
#         or (len != 0 and head != None and tail != None and head.prev == None and tail.next == None)
# You do not have to call your data members head/tail, but should be descriptive names
class linked_list :

    ## constructor - iterable is an iterable object that initializes
    #  the linked_list in the order iterable is traversed
    def __init__(self, iterable = []) :
        pass

    ## constant time access to first/last node, respectively
    #  @returns the first/last node, respectively
    def front(self) : pass
    def back(self) : pass

    ## constant time insertion of a data item (any element)
    #  as the first/last (respectively) element 
    def push_front(self, item) : pass
    def push_back(self, item) : pass

    ## constant time removal of the first/last (respectively) node/item
    #  @returns the item (not the node)
    def pop_front(self) : pass
    def pop_back(self) : pass

    ## Turns list into a string representation.
    #  Strings prints identical to how 
    #  it would if it were a Python list
    #  @returns the string representation 
    def __str__(self) : pass

    ## Provides an iterator over an instance of the linked list
    #  iterator is a separate class (either external or inner)
    #  that iterates from first to last.
    # __next__ returns a node
    #  @returns an iterator
    def __iter__(self) : pass

    ## Generator function to iterate over the linked list from last to first.
    #  Generates nodes.
    def __reversed__(self) : pass

    ## converts linked list to a bool
    #  @returns False if empty, True otherwise
    def __bool__(self) : pass

    ## Computes length of linked list
    #  @returns the length of the linked list 
    def __len__(self) : pass

    ## implements Python sequence-style equality and less-then, respectively
    #  Ensures other is another linked list, if not assertion fail
    #  @returns True if equal/less-than, False otherwise
    def __eq__(self, other) : pass
    def __lt__(self, other) : pass

    ## implements in operator
    #  @returns True if item is in linked-list, False otherwise
    def __contains__(self, item) : pass

    ## insert_after and remove are extra credit (5 points)
    #  All or nothing, linked-list must function perfectly to be elligible
    #  No partial credit

    ## constant time insertion of the data item (any element) after node
    #  @pre (precondition) node is in the linked list (self)
    def insert_after(self, node, item) : pass


    ## constant time removal of node from the linked list (self)
    #  @pre (precondition) node is in the linked list (self)
    def remove(self, node) : pass
