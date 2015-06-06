import numpy as np


#Question 1c)

def average_temp_above_height(temps, zcoords, height):
    """
    np.ndarray(np.ndarray(np.ndarray(float))), np.ndarray(float), float -> float

    Produces average temperatures above given height.

    >>> temps = np.array([[[1.0, 1.0], [2.0, 2.0]],
    ...                   [[2.0, 2.0], [3.0, 3.0]],
    ...                   [[3.0, 3.0], [4.0, 4.0]]])
    >>> zcoords = np.array([0.0, 15.0, 35.0])
    >>> act = average_temp_above_height(temps, zcoords, 15.0)
    >>> exp = 3.5
    >>> abs(exp - act) < EPS * exp
    True

    >>> act = average_temp_above_height(temps, zcoords, 10.0)
    >>> exp = 3.0
    >>> abs(exp - act) < EPS * exp
    True
    """
    s = zcoords[:]
    if s[:] > height: 
        
    
            


# Question 1e)

#def max_temps_by_height(temps):
#    """
#    np.ndarray(np.ndarray(np.ndarray(float))) -> np.ndarray(float)
#
#    Produces an array of maximum temperatures at each height in temps.
#
#    >>> temps = np.array([[[1.0, 1.0], [2.0, 2.0]],
#    ...                   [[2.0, 5.0], [4.0, 3.0]],
#    ...                   [[6.0, 5.0], [4.0, 3.0]]])
#    >>> act = max_temps_by_height(temps)
#    >>> exp = np.array([2.0, 5.0, 6.0])
#    >>> np.all(abs(exp - act) < EPS * exp)
#    True
#    """
#    return np.zeros((temps.shape[0]))   #stub
    
    
 



# Make sure tests run when this module is run

if __name__ == "__main__":
    import doctest
    EPS = 1.0e-9
    print(doctest.testmod(verbose=False))


    # NOTE: the statements below load array data from a .npz file whenever
    # this Python file is run.  This saves us from repeatedly entering
    # this code from the Python shell window when we want to pass these
    # arrays as parameters to the functions we designed above.

    data = np.load('array_data.npz')
    temps = data['temp']
    zcoords = data['height']