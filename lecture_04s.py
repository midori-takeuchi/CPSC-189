# CPSC 189 Lecture 04s

import math

# The above import is needed as we'll be making use of some functions
# from the math module.


#Problem 1: Consider the following position function that produces the
#position of a particle given a time t according to the formula:
#p = 100 e^(-t/100) sin(2 * PI * t)

def posn(t):
    """
    Real -> Real

    Produces the position of a particle at time t

    >>> exp = 0.0
    >>> act = posn(0.0)
    >>> abs(exp - act) < EPS      
    True
    >>> exp = 0.0
    >>> act = posn(1.0)
    >>> abs(exp - act) < EPS
    True
    >>> exp = 99.750312239746
    >>> act = posn(0.25)
    >>> abs(exp - act) < EPS * exp
    True
    """
    return 100.0 * math.exp(-t / 100.0) * math.sin(2 * math.pi * t)


#Now design a function that consumes a list of times and produces a list
#of positions.  Be sure to complete the tests!

def lot_2_lopn(lot):
    """
    (listof Real) -> (listof Real)

    Produces a list of positions of a particle at the times in lot

    >>> exp = [0.0, 0.0, 0.0]
    >>> act = lot_2_lopn([0.0, 0.5, 1.0])
 

    >>> exp = [posn(0.25), posn(0.75), posn(1.25)]
    >>> act = lot_2_lopn([0.25, 0.75, 1.25])
 
 
    """
    return []    #stub




#____________________________________________

# Nested loops and nested list comprehensions


# Problem 4: Suppose we wish to model a rectangular world where the height 
# of the surface at a point (x,y) is given by the formula:

# z(x, y) = 100.0 e^-(2x^2 + y^2) sin(x + y) cos(x - y)

# The following Python function consumes an x and y coordinate and produces
# the height at that point:

def height(x, y):
    """
    Real, Real -> Real

    Produces the height of a surface at point (x, y)

    >>> act = height(0, 0)
    >>> exp = 0.0
    >>> abs(act - exp) < EPS
    True

    >>> act = height(1.0, 2.0)
    >>> exp = 0.01889985717
    >>> abs(act - exp) < EPS * exp
    True
    """
    return 100.0 * math.exp(-(2 * x**2 + y**2)) * math.sin(x + y) \
           * math.cos(x - y)


# Design a function that consumes a list of x coordinates and a list of y
# coordinates that define a 2-dimensional grid and that produces a list of
# a list of z coordinates (heights) at each point on the grid.

# Note that each of the inner lists is a list of z coordinates for a fixed 
# value of y.  So, if the list of x coordinates is [0.0, 1.0] and the list of  
# y coordinates is [0.5, 1.5], we want to produce the following list of lists 
# of z coordinates:

# [[height(0.0, 0.5), height(1.0, 0.5)],   // fixed y coord of 0.5
#  [height(0.0, 1.5), height(1.0, 1.5)]]   // fixed y coord of 1.5

# (where each of the calls to the height function is replaced with the value 
# that the function produces).

# a) Complete the design of the tests using list comprehensions
# b) Complete the design of the body of the function using a nested loop
# c) Comment out the body that you just designed and refactor a copy of it
#    using a nested list comprehension


def grid_heights(lox, loy):
    """
    (listof Real), (listof Real) -> (listof (listof Real))

    Produces the heights at each point on the grid defined by lox and loy

    >>> grid_heights([], [])
    []

    >>> act = grid_heights([0.0, 1.0], [0.5, 1.5])
    >>> exp = [[height(0.0, 0.5), height(1.0, 0.5)],
    ...        [height(0.0, 1.5), height(1.0, 1.5)]]
     
    
    
    """
    return []   #stub
    
    
    
    

#___________________________________________

#Make sure tests run when this module is run

if __name__ == "__main__":
    import doctest
    EPS = 1.0e-9
    print(doctest.testmod(verbose=False))

