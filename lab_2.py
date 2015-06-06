# CPSC 189 Lab 2

# Exercise 1: In this first exercise we work through the process of
# redesigning a function that has the recursive call in tail position, 
# to another that uses a loop.
#
# Consider the following function.  Note that it uses an accumulator
# to accumulate the result and that the recursive call is in tail
# position.

def how_many(lox, sx):
    """
    (listof X), X -> int

    Produces number of times sx is found in lox

    >>> how_many([], 4)
    0

    >>> how_many(['a', 'b', 'c'], 'd')
    0
    
    >>> how_many(['a', 'b', 'a'], 'a')
    2
    """
    if lox == []:
        return 0
    else:
        if lox[0] == sx:
            return 1 + how_many(lox[1:], sx)
        else:
            return how_many(lox[1:], sx)


# Redesign the function again so that it uses a loop (call this
# redesigned version how_many2)

def how_many2(lox, sx):
    """
    (listof X), X -> int

    Produces number of times sx is found in lox

    >>> how_many([], 4)
    0

    >>> how_many(['a', 'b', 'c'], 'd')
    0
    
    >>> how_many(['a', 'b', 'a'], 'a')
    2
    
    Accumulator: acc is int
    
    Invariant: number of times sx is found in lox so far
    """
    acc = 0
    
    for string in lox:
        if string == sx:
            acc = acc + 1
            
    return acc




# Exercise 2: Consider the function from_list (below) that consumes a
# non-empty list of the digits of a non-negative integer and produces that
# integer. (Note that Natural is not a primitive data type in Python.
# We use it to represent natural numbers, just as you did in CPSC 110.)

def from_list(nelon0):
    """
    (nelistof Natural) -> Natural

    Produces a non-negative integer constructed from the digits in nelon0

    >>> from_list([7])
    7

    >>> from_list([5, 3, 0, 2])
    5302
    """

    def from_list_acc(nelon, acc):
        """
        Accumulator: acc is Natural

        Invariant: acc is the number constructed from the elements of nelon0
        prior to nelon[0]

        from_list_acc([7, 1, 4], 0)
        from_list_acc([1, 4], 7)
        from_list_acc([4], 71)
        """
        if nelon[1:] == []:
            return nelon[0] + 10 * acc
        else:
            return from_list_acc(nelon[1:], nelon[0] + 10 * acc)

    return from_list_acc(nelon0, 0)


# Redesign the function from_list using a loop rather than recursion.
# Call the redesigned function from_list2

def from_list2(nelon0):
    """
    (nelistof Natural) -> Natural

    Produces a non-negative integer constructed from the digits in nelon0

    >>> from_list([7])
    7

    >>> from_list([5, 3, 0, 2])
    5302
    
    Accumulator: acc is Natural
    
    Invariant: acc is the number contructed from the elements of nelon0 seen
    so far
    """
    acc = 0
    
    for n in nelon0:
        acc = n + 10 * acc
        
    return acc




# Exercise 3: Design a function that consumes a (listof X) and produces
# a (listof X) with the items from the given list in reverse order.  Design
# your function directly using a loop.  Think about what you need to accumulate
# as the list is processed.

def reverse(lox):
    """
    listof X -> listof X
    
    Consumes a listof X and produces a list with those items in reverse order
    
    >>> reverse([])
    []
    
    >>> reverse([1])
    [1]
    
    >>> reverse([1, 2])
    [2, 1]
    
    Accumulator: acc is listof X
    
    Invariant: acc is the list of the items reversed seen so far
    """
    
    acc = []
    for x in lox: 
        acc = [x] + acc
        
    return acc
    



# *** Designing with list comprehensions ***

# Exercise 4: using a list comprehension, design a function that consumes
# a list of float and an integer N and produces a list of those floats
# rounded to N decimal places.
#
# Hint: examine the documentation for Python built-in functions to
# find a suitable helper.
# http://docs.python.org/3.4/library/functions.html

def round_lof(lof, N):
    """
    listof Float, int -> listof Float
    
    Consumes a list of float and an integer N and produces a list of those floats
    rounded to N decimal places
    
    >>> round_lof([], 1)
    []
    
    >>> round_lof([1.12, 2.521], 1)
    [1.1, 2.5]
    
    Accumulator: acc is listof Float
    
    Invariant: acc is the listof Float rounded to N decimal places seen so far
    """
    
#    acc = []
#    for f in lof: 
#        acc = acc + [round(f, N)]
#    
#    return acc
    
    acc = [round(f, N) for f in lof]
    
    return acc
    



# Exercise 5: using a list comprehension, design a function that consumes a
# list of lists of integers and produces a list of lists of integers where
# the integers in each list are sorted in increasing order.
#
# Hint: look at the documentation for built-in functions for a useful helper!

def increasing_order(loloi):
    """
    listof listof int -> listof listof int
    
    Consumes a list of lists of intengers and produces a list of lists of 
    integers where the integers in each list are sorted in increasing order
    
    >>> increasing_order([[], []])
    [[], []]
    
    >>> increasing_order([[3, 2], [5, 8]])
    [[2, 3], [5, 8]]
    
    >>> increasing_order([[9, 7, 6], [3, 1]])
    [[6, 7, 9], [1, 3]]
    
    Accumulator: acc is a list of lists of integers
    
    Invariant: acc is a list of lists of integers in increasing order seen
    so far
     
    """
    
#    acc = []
#    for loi in loloi:
#        acc = acc + [sorted(loi)]
#        
#    return acc
    
    acc = [sorted(loi) for loi in loloi]
    
    return acc
        

        

# Exercise 6: using a list comprehension, design a function that consumes
# a list of integers and a threshold value (also an integer). The function
# produces True if at least one integer in the list is higher than the
# threshold value and False otherwise.









# Exercise 7: using a list comprehension, design a function that consumes a
# list of words and a word size.  The function produces true if
# all the words have length greater than the given word size
# and false otherwise.
#
# Hint: look at the documentation for built-in functions for a useful helper!


# Here is the data definition for Word:

# Word is str
# interp. a word











# Exercise 8: Consider the following data definition:

# Person is dict(name=String, age=int, city=String)
# interp. a person with a name, age and city of residence

P1 = dict(name='Chris', age=44, city='Nanaimo')
P2 = dict(name='Pat', age=17, city='Vancouver')
P3 = dict(name='Jin', age=25, city='Vancouver')
P4 = dict(name='Xin', age=34, city='Vancouver')

# Using a list comprehension, design a function that consumes a list of Person
# and that determines if all the people in the list are eligible to vote in a
# civic election.  To be eligible to vote a Person must reside in Vancouver
# and be at least 18 years of age.











# Make sure the doctests run when this script is run.

if __name__ == '__main__':
    import doctest
    print(doctest.testmod(verbose=False))