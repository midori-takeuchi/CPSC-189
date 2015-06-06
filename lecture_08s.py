# CPSC 189 Lecture 08 Starter

import numpy as np
import matplotlib.pyplot as pyplt


# Exercise 1

def zero_neg(arr):
    """
    np.ndarray(Real) -> NoneType
 
    Effect: modifies arr so that all negative values are replaced with zero.
 
    >>> arr = np.array([1.0, -2.0, 3.0, -4.0, 5.0])
    >>> zero_neg(arr)
    >>> exp = np.array([1.0, 0.0, 3.0, 0.0, 5.0])
    >>> np.array_equal(arr, exp)
    True
    """
    arr[arr < 0] = 0


# Exercise 2:

def num_in_range(arr, t):
    """
    np.ndarray(Real), Real -> int

    Determines the number of elements in arr below t

    >>> arr = np.array([1.0, -2.0, 3.4, -4.8, 5.1])
    >>> num_in_range(arr, 3.0)
    3
    """
    return np.size(arr[arr < t])


# Exercise 3: 

def sum_positive(arr):
    """
    np.ndarray(Real) -> Real

    Determines the sum of the positive entries of arr
    
    >>> arr = np.array([2, 4, -5, 0, 1])
    >>> sum_positive(arr)
    7

    >>> arr = np.array([1.0, -2.0, 3.4, -4.8, 5.1])
    >>> act = sum_positive(arr)
    >>> exp = 9.5
    >>> abs(act - exp) < EPS * exp
    True
    """
    return sum(arr[arr > 0])


# Exercise 4:

def position_arr(t_arr, a, d):
    """
    np.ndarray(float), float, float -> np.ndarray(float)
    
    Produces an array of positions of a particle for each t in t_arr,
    according to the formula: p = a * exp(-t * d) * sin(2 * pi * t)
    
    >>> act = position_arr(np.array([]), 100.0, 0.1)
    >>> exp = np.array([])
    >>> np.array_equal(act, exp)
    True
    
    >>> act = position_arr(np.array([0.1, 0.2, 0.3]), 100.0, 0.1)
    >>> exp = np.array([58.19366913, 93.22243355, 92.29485483])
    >>> np.all(np.abs(act-exp) < EPS * exp)
    True
    >>> 
    """
    return a * np.exp(-t_arr * d) * np.sin(2 * (np.pi * t_arr))
    
    

# Exercise 5:

#==============================================================================
# def plot_posn(t_arr, loargs):
#     """
#     np.ndarray(float), (listof (float, float)) -> NoneType
#     
#     Generates a plot of position against time for each t in t_arr
#     and for each (a, d) in loargs where a and d are arguments
#     for the position function:
#          p = a * exp(-t * d) * sin(2 * pi * t)
#     """
#     pyplt.plot(t_arr, )
#==============================================================================

    
    
    


# Make sure tests run when this module is run

if __name__ == "__main__":
    import doctest
    EPS = 1.0e-9
    print(doctest.testmod(verbose=False))
