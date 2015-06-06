# CPSC 189  Lab 05

# Working with the numpy library

import numpy as np
import matplotlib.pyplot as pyplt


#Q1. Design a function that consumes a 1D array of pressures and a
#    corresponding 1D array of heights and that produces a chart of pressure
#    against height.  Label your axes and include appropriate units.  (You
#    can get units of measurement from the 'var_descrip' array.)

def plot_pressure(press, zcoords):
    """
    np.array(float), np.array(float) -> NoneType

    Effect: produces chart of height against pressure
    """
    pyplt.plot(press, zcoords, 'b-')
    pyplt.xlabel('Pressure(hPa)')
    pyplt.ylabel('Height(m)')
    pyplt.show()



#Q2. Now make a call to your function from the Python shell and save
#    your chart as a .png file.





#Q3.  Design a function that consumes a 3D array of data shaped like the TABS,
#     QV or W arrays.  Each entry in the array is a 2D array that represents
#     data at a particular height.  The function also consumes a 1D array of
#     heights and a float representing a particular height.  The function must
#     return a 2D array containing only those temperatures that are at the
#     specified height.

#     Note: give that the heights are represented as floats be careful not to
#     expect an exact match between the given height and the heights stored
#     in the array.

#     Also note: the test is not complete!  First complete the test before
#     replacing the stub with the function body.

def extract_data_at_height(data, zcoords, at_height):
    """
    np.array(np.array(np.array(float)))), np.array(float), float
    -> np.array(np.array(float))

    >>> data = np.array([[[1.0, 1.0], [1.0, 1.0]],
    ...                  [[2.0, 2.0], [2.0, 2.0]],
    ...                  [[3.0, 3.0], [3.0, 3.0]]])
    >>> zcoords = np.array([0.0, 20.0, 40.0])
    >>> got = extract_data_at_height(data, zcoords, 20.0)
    >>> want = np.array([[2.0, 2.0], [2.0, 2.0]])
    >>> np.all(abs(got - want) < EPS)
    True
    """
    x = np.abs(zcoords - at_height) < EPS
    return data[x] 
    


#Q4. Design a function that consumes a 3D array of data shaped like the TABS,
#    QV or W arrays.  Each entry in the array is a 2D array that represents
#    data at a particular height.  The function also consumes a 1D array of
#    heights and a float representing a particular height.  The function must
#    return the maximum value of the data at the specified height.

#    Note: given that the heights are represented as floats be careful not to
#    expect an exact match between the given height and the heights stored
#    in the array.

def max_at_height(data, zcoords, at_height):
    """
    np.array(np.array(np.array(float)))), np.array(float), float
    -> float
    >>> temps = np.array([[[1.0, 1.0], [1.0, 1.0]],
    ...      [[2.0, 3.0], [4.0, 5.0]],
    ...      [[6.0, 6.0], [6.0, 6.0]]])
    >>> zcoords = np.array([10.0, 20.0, 30.0])
    >>> max_at_height(temps, zcoords, 20.0)
    5.0
    """
    return np.max(extract_data_at_height(data, zcoords, at_height))


#Q5. Design a function that consumes a 3D array of data shaped like the TABS,
#    QV or W arrays - let's assume it's called data.  Each entry in the array is
#    a 2D array that represents data at a particular height. The function must
#    produce a 1D array, let's refer to it as avg, such
#    that:

#    avg[i] = average of the data in the 2D array data[i]

#    for all valid indices, i

#    In other words, each entry in avg represents an average over a horizontal
#    slice through the 3D array.

#    Also note: the test is not complete!  First complete the test before
#    replacing the stub with the function body.

def horizontal_avg(arr):
    """
    np.array(np.array(np.array(float))) -> np.array(float)

    Produces array of averages over horizontal slices of arr.

    >>> test = np.array([[[1.0, 2.0], [2.0, 2.0], [2.0, 1.0]],
    ...                  [[5.0, 6.0], [6.0, 6.0], [6.0, 5.0]],
    ...                  [[3.0, 4.0], [4.0, 4.0], [4.0, 3.0]]])
    >>> got = horizontal_avg(test)
    >>> want = np.array([1.666666667, 5.666666667, 3.666666667])
    >>> np.all(abs(got-want) < EPS)
    True
    """
    
    return arr.mean(axis=2).mean(axis=1)
    #return np.zeros((arr.shape[0]))  #stub


#Q6. Design a function that consumes a 3D array of temperatures and
#    produces a chart of height against the horizontal averages of 
#    temperatures.  Provide a suitable title and labels for your
#    axes.

def plot_mean_temp(temps, zcoords):
    """
    np.array(np.array(np.array(float))), np.array(float) -> NoneType

    Effect: plots height against horizontal average of temperature
    """
    pyplt.plot(horizontal_avg(temps), zcoords, 'b-')
    pyplt.title('Mean Temperature by Height')
    pyplt.xlabel('Height(m)')
    pyplt.ylabel('Mean Temperature(K)')
    pyplt.show()


#Q7. Call your function from the Python Shell and save your chart as a .png file






#Q8. Design a function that produces a contour plot of the perturbation of a
#    2D array of data from the average of the data in that array.  In other
#    words, we wish to graph how much each value in the 2D array differs
#    from the average value of all the data in the array.  The function
#    also consumes two 1D arrays representing the x and y coordinates
#    that define the grid where the data in the 2D array were measured.
#    These coordinates must be used to label tick marks on the axes.
#    The function also consumes 3 strings representing labels for the x and y
#    axes and a title for the chart. Label the contours inline with a font
#    size of 12.

#===============================================================================
# def contour_plot(data, xcoords, ycoords, title, xlabel, ylabel):
#     """
#     np.array(np.array(float)), np.array(float), np.array(float),
#     str, str, str -> NoneType
# 
#     Effect: produces a contour plot of perturbations from average for
#     given data.
#     """
#     return None    #stub
#===============================================================================


#Q9. Now call your function from the Python shell to generate contour plots
#    for the perturbation of temperatures from the average at heights 1950 
#    and 2850.  Save your plots to .png files.  There is no need to design 
#    a function to do this - just enter the necessary statements in the 
#    Python shell.






#Q10. Design a function that consumes a 3D array of temperatures, a 3D
#     array of vertical velocities, a 1D array of heights and a particular
#     height.  The function produces the average temperature at the given
#     height for those points where there is an updraft (points where the
#     vertical velocity is positive).

#===============================================================================
# def ave_temp_updraft(temps, zvels, zcoords, at_height):
#     """
#     np.array(np.array(np.array(float))), np.array(np.array(np.array(float))),
#     np.array(float), float -> float
# 
#     Produces the average temperature at a given height at points where
#     there is an updraft.
# 
#     >>> temps = np.array([[[1.0, 2.0], [2.0, 2.0], [2.0, 1.0]],
#     ...                   [[5.0, 6.0], [6.0, 6.0], [6.0, 5.0]],
#     ...                   [[3.0, 4.0], [4.0, 4.0], [4.0, 3.0]]])
#     >>> zvels = np.array([[[1.0, 1.0], [-1.0, -1.0], [1.0, -1.0]],
#     ...                   [[1.0, -1.0], [1.0, 1.0], [-1.0, -1.0]],
#     ...                   [[-1.0, -1.0], [-1.0, 1.0], [1.0, 1.0]]])
#     >>> zcoords = np.array([0, 10, 20])
#     >>> got = ave_temp_updraft(temps, zvels, zcoords, 10)
#     >>> want = 17.0 / 3.0
#     >>> abs(want - got) < EPS * want
#     True
# 
#     >>> got = ave_temp_updraft(temps, zvels, zcoords, 0)
#     >>> want = 5.0 / 3.0
#     >>> abs(want - got) < EPS * want
#     True
#     """
#     return 0.0    #stub
#===============================================================================


#Q11. Now make calls to your function from the Python shell to determine the
#     average temperature at updraft points at a height of 850 and 1950m.





# Make sure tests run when this module is run

# Also load the data file 'sim_data.npz' and extracts data as np.array

if __name__=='__main__':
    import doctest
    EPS = 1.0e-9
    print(doctest.testmod(verbose=False))

    sim_data = np.load('sim_data.npz')
    temps = sim_data['TABS']
    zvels = sim_data['W']
    zcoords = sim_data['z']
    xcoords = sim_data['x']
    ycoords = sim_data['y']
    press = sim_data['p']