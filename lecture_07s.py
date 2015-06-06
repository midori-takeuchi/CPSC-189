# CPSC 189 Lecture 07 Starter

from math import sin, exp, pi
import matplotlib.pyplot as pyplot

# Question 1.
# a)

def position1(t):
    """
    Real -> Real

    Produces the position of a particle at time t

    >>> exp = 0.0
    >>> act = position1(0.0)
    >>> abs(exp - act) < EPS
    True
    >>> exp = 0.0
    >>> act = position1(1.0)
    >>> abs(exp - act) < EPS
    True
    >>> exp = 97.5309912028
    >>> act = position1(0.25)
    >>> abs(exp - act) < EPS * exp
    True
    """
    return 100.0 * exp(-t * 1.0 / 10.0) * sin(2 * pi * t)


def position2(t):
    """
    Real -> Real

    Produces the position of a particle at time t

    >>> exp = 0.0
    >>> act = position2(0.0)
    >>> abs(exp - act) < EPS
    True
    >>> exp = 0.0
    >>> act = position2(1.0)
    >>> abs(exp - act) < EPS
    True
    >>> exp = 94.3023340076
    >>> act = position2(0.25)
    >>> abs(exp - act) < EPS * exp
    True
    """
    return 98.0 * exp(-t * 2.0 / 13.0) * sin(2 * pi * t)
    
def position(t, x, y):
    """
    Real -> Real

    Produces the position of a particle at time t

    >>> exp = 0.0
    >>> act = position(0.0, 100.0, (1.0 / 10.0))
    >>> abs(exp - act) < EPS
    True
    >>> exp = 0.0
    >>> act = position(1.0, 100.0, (1.0 / 10.0))
    >>> abs(exp - act) < EPS
    True
    >>> exp = 97.5309912028
    >>> act = position(0.25, 100.0, (1.0 / 10.0))
    >>> abs(exp - act) < EPS * exp
    True
    >>> exp = 94.3023340076
    >>> act = position(0.25, 98.0, (2.0 / 13.0))
    >>> abs(exp - act) < EPS * exp
    True
    """
    return x * exp(-t * y) * sin(2 * pi * t)
    
# b)
    
def list_posns(lot, x, y):
    """
    listof Real, Real, Real -> listof Position
    
    Produces a list of positions at a time t, amplitude amp, and damping factor
    damp.
    
    >>> exp = [0.0]
    >>> act = list_posns([0.0], 2.0, 1.0)
    >>> abs(exp - act) < EPS * exp
    True
    >>> exp = [0.0, 0.0]
    >>> act = list_posns([0.0, 1.0], 100.0, (1.0 / 10.0))
    >>> abs(exp - act) < EPS * exp
    True
    >>> exp = [0.0, 0.0, 94.3023340076]
    >>> act = list_posns([0.0, 1.0, 0.25], 98.0, (2.0 / 13.0))
    >>> abs(exp - act) < EPS * exp
    True
    """
    return [position(t, x, y) for t in lot]


# c)

#==============================================================================
# def posn_plot(lot, loargs):
#     """
#     (listof Real), (listof (Real, Real, str)) -> NoneType
# 
#     Effect: generates a plot of position against time for each set of
#     arguments in loargs.
#     """
#     pyplot.plot(lot,)
#==============================================================================


# Question 2

#def foldl(fn, base, lox):
#    """
#    (X, Y -> Y), Y, (listof X) -> Y
#    
#    Produces fn(xn, ... f(x1, base)) where x1, ..., xn are values in lox;
#    produces base if list is empty
#    
#    >>> foldl(lambda a, b: a + b, 5, [])
#    
#    
#    >>> foldl(lambda a, b : a + b, 0, [1, 2, 3, 4])
#    
#    
#    >>> foldl(lambda a, b : str(a) + b, "", [1, 2, 3])
#    
#    """









# Question 3
#def poly_posn(t):
#    """
#    Real -> Real
#
#    Produces the position of a particle at time t
#
#    >>> exp = 0.0
#    >>> act = poly_posn(0.0)
#    >>> abs(exp - act) < EPS
#    True
#
#    >>> exp = 87.99971411132
#    >>> act = poly_posn(1.25)
#    >>> abs(exp - act) < EPS * exp
#    True
#    """
#    return 4187.0222 * t**6 - 18705.0667 * t**5 + 29582.2222 * t**4 \
#           - 18944.0000 * t**3 + 3606.7555 * t**2 + 273.0667 * t
#
#
#def abs_lot_2_lopn(position_fn, lot, *args):
#    """
#    (Real, ... -> Real), (listof Real), ... -> (listof Real)
#
#    Consumes a position function, list of times and arbitrary length argument
#    list and produces a list of positions at the given times
#
#    >>> abs_lot_2_lopn(lambda t : 2 * t, [])
#    []
#
#    >>> abs_lot_2_lopn(lambda t : 2 * t, [4])
#    [8]
#
#    >>> act = abs_lot_2_lopn(lambda t, a : a * t,
#    ...                     [0.0, 0.1, 0.2], 3.0)
#    >>> exp = [0.0, 0.3, 0.6]
#    >>> all([abs(e - a) < EPS for (e, a) in zip(exp, act)])
#    True
#    """
#    return []



# Question 4

#def plot_posn_fn(lofnargs, lot):
#    """
#    (listof ((Real, ... -> Real), (...), str)), (listof Real) -> NoneType
#
#    Effect: generates a plot of position against time for each set of
#    position function and associated arguments in lofnargs
#    """
#    return None



# Make sure tests run when this module is run

if __name__ == '__main__':
    import doctest
    EPS = 1.0e-9  # for testing floats
    print(doctest.testmod(verbose=False))

