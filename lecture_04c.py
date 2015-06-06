# Lecture 04

import math

#Example: Consider the following position function that produces the
#position of a particle given a time t according to the formula:
#p = 100 e^(-t/100) sin(2 * PI * t)

#***
#Note that we imported the math module at the top of this file.  This
#is necessary if we are to call functions like math.sin, math.exp from
#the math module.
#***

def posn(t):
    """
    Real -> Real

    Produces the position of a particle at time t

    >>> exp = 0.0
    >>> act = posn(0.0)
    >>> abs(exp - act) < EPS      #<---NOT: (EPS * want)   Why?
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
#of positions.

#***
#Note the use of list comprehensions in formulating the tests below!
#***

def lot_2_lopn(lot):
    """
    (listof Real) -> (listof Real)

    Produces a list of positions of a particle at the times in lot

    >>> exp = [0.0, 0.0, 0.0]
    >>> act = lot_2_lopn([0.0, 0.5, 1.0])
    >>> # Why do we NOT multiply EPS by abs(e) in the following test?
    >>> all([abs(e - a) < EPS for (e, a) in zip(exp, act)])
    True

    >>> exp = [posn(0.25), posn(0.75), posn(1.25)]
    >>> act = lot_2_lopn([0.25, 0.75, 1.25])
    >>> # Why is EPS multiplied by abs(e), rather than e, in the following test?
    >>> all([abs(e - a) < EPS * abs(e) for (e, a) in zip(exp, act)])
    True
    """
    return [posn(t) for t in lot]

#____________________________________________

# Nested loops and nested list comprehensions

# Example: Terrain models.

# Suppose we wish to model a rectangular world where the height of the surface
# at a point (x,y) is given by the formula:

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

# a) Complete the design of the tests
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
    >>> all([abs(a - e) < EPS * abs(e) for (loa, loe) in zip(act, exp)
    ...        for (a, e) in zip(loa, loe)])
    True
    """
    #1. For each y coordinate, compute a list of heights lying along one row
    #add accumulate in 'heights'

    #heights = []
    #for y in loy:
        #<compute row of heights -> row_heights>
        #heights = heights + [row_heights]

    #2. Now figure out how to compute a list of heights lying along a
    #single row

    #heights = []
    #for y in loy:
        #row_heights = []
        #for x in lox:
            #row_heights = row_heights + [height(x,y)]
        #heights = heights + [row_heights]

    #return heights

    #3. Notice that we have a nested loop (one loop inside another) and
    #   that this represents a complete solution to the problem. 
    #   We're now going to refactor this code using a nested list
    #   comprehension.
    
    #   First we refactor the inner loop...
    
    #heights = []
    #for y in loy:
        #row_heights = [height(x,y) for x in lox]
        #heights = heights + [row_heights]

    #return heights

    #4. Eliminate the use of the variable row_heights

    #heights = []
    #for y in loy:
        #heights = heights + [[height(x,y) for x in lox]]

    #return heights

    #5. Refactor the remaining loop to use a list comprehension

    #heights = [[height(x,y) for x in lox] for y in loy]
    #return heights

    #6. Eliminate the use of the variable heights

    return [[height(x, y) for x in lox] for y in loy]



#Make sure tests run when this module is run

if __name__ == "__main__":
    import doctest
    EPS = 1.0e-9
    print(doctest.testmod(verbose=False))

