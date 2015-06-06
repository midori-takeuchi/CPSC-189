# Lecture 03

# From recursion to iteration...
# In today's lecture we investigate how to design functions using loops...

# Consider the following function from Lecture 02:

#def sum_positive(loi0):
#    """
#    (listof int) -> int
#
#    Produces the sum of the positive integers in loi
#
#    >>> sum_positive([])
#    0
#
#    >>> sum_positive([5, -4, 3])
#    8
#    """
#    def sum_positive_acc(loi, acc):
#        """
#        Accumulator: acc is int
#
#        Invariant: acc represents the sum of the positive integers in loi0
#        prior to loi[0]
#
#        sum_positive_acc([5, -4, 3], 0)
#        sum_positive_acc([-4, 3], 5)
#        sum_positive_acc([3], 5)
#        sum_positive_acc([], 8)
#        """
#        if loi == []:
#            return acc
#        else:
#            if loi[0] > 0:
#                return sum_positive_acc(loi[1:], loi[0] + acc)
#            else:
#                return sum_positive_acc(loi[1:], acc)
#
#    return sum_positive_acc(loi0, 0)

# We start by re-designing this function using a loop...

def sum_positive(loi):
    """
    (listof int) -> int

    Produces the sum of loi

    >>> sum_positive([])
    0

    >>> sum_positive([5, -4, 3])
    8
    
    Accumulator: acc is int

    Invariant: acc is the sum of the positive integers processed so far

    Example: sum_positive([5, -4, 3])
    Processed so far       Accumulator
    []                     0
    [5]                    5
    [5, -4]                5
    [5, -4, 3]             8
    """

    acc = 0

    for num in loi:
        if num > 0:
            acc = acc + num

    return acc

#Try the following in the Python Shell window:
#sum_positive(list(range(-100,100)))      # should produce expected result
#sum_positive(list(range(-1500,1500)))    # also produces expected result!

#_____________________________________

# Problem 1: complete the design of the following function using a loop

def average_lon(lon):
    """
    (nelistof Real) -> float

    Determines the average of a non-empty list of numbers

    >>> exp = 2.0
    >>> act = average_lon([2.0])
    >>> abs(exp - act) < EPS * exp
    True

    >>> exp = 3.0
    >>> act = average_lon([2.0, 4.5, 2.5])
    >>> abs(exp - act) < EPS * exp
    True

    >>> exp = 3.5
    >>> act = average_lon([2, 4, 3, 5])
    >>> abs(exp - act) < EPS * exp
    True
    
    Accumulator: sum_acc is real
    Invariant: sum_acc is the sum of the list of reals seen so far
    
    Accumulator: total_acc is real
    Invariant: total_acc is the number of reals seen so far
    
    Example: average_lon([2.0, 4.5, 2.5])
    Processed so far    sum_acc     total_acc
    []                  0           0
    [2.0]               2.0         1
    [2.0, 4.5]          6.5         2
    [2.0, 4.5, 2.5]     9.0         3
    
    """
    sum_acc = 0.0
    total_acc = 0.0
    
    for num in lon: 
        sum_acc = sum_acc + num
        total_acc = total_acc + 1
        
    return sum_acc / total_acc
        

# The previous example illustrates the fact that sometimes we want to
# accumulate more than one value as we process a list.



#_____________________________________

# Problem 2: Design a function that consumes a list of string and produces
# a list of the lengths of those strings

def str_lengths(los):
    """
    (listof str) -> (listof int)

    Produces a list of the lengths of a list of strings

    >>> str_lengths([])
    []

    >>> str_lengths([''])
    [0]

    >>> str_lengths(['123'])
    [3]

    >>> str_lengths(['1', '12', '123'])
    [1, 2, 3]
    
    Accumulator: acc is listof int
    Invariant: acc is the list of the lengths of the strings seen so far
    
    Example: str_lengths(['1', '12', '123'])
    Processed so far    Accumulator
    []                  []
    ['1']               [1]
    ['1', '12']         [1, 2]
    ['1', '12', '123']  [1, 2, 3]


    """
    acc = []
    
    for str in los:
        acc = acc + [len(str)]
        
    return acc


#_____________________________________

# Problem 3: Design a function that consumes two lists of pressures (same length)
# and a tolerance (a Real) and produces a list of pairs (tuples) of
# pressures whose difference in absolute value is greater than the tolerance.

def pressure_diff(lop1, lop2, tol):
    """
    (listof Real), (listof Real), Real -> (listof (Real, Real))

    >>> pressure_diff([], [], 0.001)
    []

    >>> pressure_diff([0.4], [0.40001], 0.0001)
    []

    >>> pressure_diff([0.4], [0.39998], 0.00001)
    [(0.4, 0.39998)]

    >>> pressure_diff([0.4, 0.5, 0.6, 0.7], [0.395, 0.489, 0.605, 0.711], 0.01)
    [(0.5, 0.489), (0.7, 0.711)]

    Accumulator:  lopp is (listof (Real, Real))
    
    Invariant: lopp is a list of pairs of pressures from zip(lop1, lop2)
    whose difference in absolute value is greater than tol, that have been
    processed so far
    
    Example: pressure_diff([0.5, 0.6, 0.7], [0.489, 0.605, 0.711], 0.01)
    processed so far                          accumulator
    []                                        []
    [0.5] [0.489]                             [(0.5, 0.489)]
    [0.5, 0.6] [0.489, 0.605]                 [(0.5, 0.489)]
    [0.5, 0.6, 0.7] [0.489, 0.605, 0.711]     [(0.5, 0.489), (0.7, 0.711)]
    """
    lopp = []

    for (p1, p2) in zip(lop1, lop2):
        if abs(p1 - p2) > tol:
            lopp = lopp + [(p1, p2)]

    return lopp


#_____________________________________

# Make sure doctests run when script is run

if __name__ == '__main__':
    import doctest
    EPS = 1.0e-9  # for testing equality on floats
    print(doctest.testmod(verbose=False))


