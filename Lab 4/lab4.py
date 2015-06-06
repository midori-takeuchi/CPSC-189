# CPSC 189, Lab 04 - File I/O

from io import StringIO
import matplotlib.pyplot as pyplot

# Global assumptions: files have expected number of header rows and
# data in file is separated by specified delimiter.  There is at least one
# row of data in the file.  There could be rows that contain only
# whitespace (spaces or tabs or newlines).

# The following functions from lecture and the previous lab are provided 
# for use in this lab:

def skip_rows(f, num_rows):
    """
    file, int -> NoneType

    Effect: skips over next num_rows rows in file

    >>> test_file = StringIO('row1\\n row2\\n row3\\n row4\\n')
    >>> skip_rows(test_file, 3)
    >>> test_file.readline()
    ' row4\\n'
    """
    for row in range(num_rows):
        f.readline()



def item_in_col(line, col, delim=None):
    """
    str, int, str -> float

    Produces the float at the given column in line.
    Assume: the first column is column 0
    Requires: line is a string containing numbers separated by delim

    >>> item_in_col('0.0, 1.1, 2.2, 3.3, 4.4, 5.5', 4, ',')
    4.4
    >>> item_in_col('0.0 1.1 2.2 3.3 4.4 5.5', 3)
    3.3
    """
    data = line.split(delim)
    return float(data[col])

#____________________________________________________________________________

# In the questions that follow, we assume that we are working
# with Environment Canada data in the file yvr_2011.csv (or a similarly
# formatted file) which we assume is in the same directory as this Python
# source file.

# Be sure to account for the fact that there may be empty lines in the file.

#____________________________________________________________________________

# Q1. Consider the following functions designed in the previous lab:

def max_col(f, col, delim=None, nhr=0):
    """
    file, int, str, int -> float

    Produces the maximum value of data stored in given column of file f

    >>> test_file = StringIO('row1\\n row2\\n 0, 1, 2, 3, 4, 5, 6, 7\\n  \\n')
    >>> max_col(test_file, 5, ',', 2)
    5.0

    >>> test_file = StringIO('row1\\n row2\\n 0 1 2 3 4 5 6 7\\n' \
                             '10 11 12 13 14 15 16 17\\n  \\n')
    >>> max_col(test_file, 5, nhr=2)
    15.0
    """
    skip_rows(f, nhr)

    return max([item_in_col(line, col, delim) for line in f
               if line.strip() != ''])


def tot_col(f, col, delim=None, nhr=0):
    """
    file, int, str, int -> Real

    Produces the sum of data stored in given column of file f

    >>> test_file = StringIO('row1\\n row2\\n 0, 1, 2, 3, 4, 5, 6, 7\\n  \\n')
    >>> tot_col(test_file, 5, ',', 2)
    5.0

    >>> test_file = StringIO('row1\\n row2\\n 0 1 2 3 4 5 6 7\\n' \
                             '  \\n10 11 12 13 14 15 16 17\\n')
    >>> tot_col(test_file, 5, nhr=2)
    20.0
    """
    skip_rows(f, nhr)

    return sum([item_in_col(line, col, delim) for line in f
               if line.strip() != ''])


# Note the similarity between these two functions.  Design a more abstract
# function that is capable of determining the max or sum (or any other
# computation that consumes a list of float and produces a float) of a 
# specified column of data of type Real.

def fn_col(fn, f, col, delim=None, nhr=0):
    """
    file, int, str, int -> float

    Produces a float from applying a function to a specified colum of data
    of type Real

    >>> test_file = StringIO('row1\\n row2\\n 0, 1, 2, 3, 4, 5, 6, 7\\n  \\n')
    >>> fn_col(max, test_file, 5, ',', 2)
    5.0

    >>> test_file = StringIO('row1\\n row2\\n 0 1 2 3 4 5 6 7\\n' \
                             '10 11 12 13 14 15 16 17\\n  \\n')
    >>> fn_col(max, test_file, 5, nhr=2)
    15.0
    
     >>> test_file = StringIO('row1\\n row2\\n 0, 1, 2, 3, 4, 5, 6, 7\\n  \\n')
    >>> fn_col(sum, test_file, 5, ',', 2)
    5.0

    >>> test_file = StringIO('row1\\n row2\\n 0 1 2 3 4 5 6 7\\n' \
                             '  \\n10 11 12 13 14 15 16 17\\n')
    >>> fn_col(sum, test_file, 5, nhr=2)
    20.0
    """
    skip_rows(f, nhr)

    return fn([item_in_col(line, col, delim) for line in f
               if line.strip() != ''])


# Q1b. Now make a call to your function from the Python Shell to determine
# the smallest min temperature over the year.

# Make a note of the call you made to your function and the value produced
# so that they can be checked by your TA:

#==============================================================================
# >>> with open('yvr_2011.csv', 'U') as f:
# ...     fn_col(min, f, 7, ',', 24)
# ... 
#==============================================================================
# -8.1





# Q1c. Rewrite the functions max_col and tot_col in terms of your newly
# designed abstract function.  Note: copy and paste everything except
# the body of the function - the signature, purpose and tests do not
# change!  Rename the functions max_col_v2 and tot_col_v2 - be sure
# to rename the function calls in your tests too!

def max_col_v2(fn, f, col, delim=None, nhr=0):
    """
    file, int, str, int -> float

    Produces the maximum value of data stored in given column of file f

    >>> test_file = StringIO('row1\\n row2\\n 0, 1, 2, 3, 4, 5, 6, 7\\n  \\n')
    >>> max_col_v2(max, test_file, 5, ',', 2)
    5.0

    >>> test_file = StringIO('row1\\n row2\\n 0 1 2 3 4 5 6 7\\n' \
                             '10 11 12 13 14 15 16 17\\n  \\n')
    >>> max_col_v2(max, test_file, 5, nhr=2)
    15.0
    """
    return fn_col(max, f, col, delim, nhr)


def tot_col_v2(fn, f, col, delim=None, nhr=0):
    """
    file, int, str, int -> Real

    Produces the sum of data stored in given column of file f

    >>> test_file = StringIO('row1\\n row2\\n 0, 1, 2, 3, 4, 5, 6, 7\\n  \\n')
    >>> tot_col_v2(sum, test_file, 5, ',', 2)
    5.0

    >>> test_file = StringIO('row1\\n row2\\n 0 1 2 3 4 5 6 7\\n' \
                             '  \\n10 11 12 13 14 15 16 17\\n')
    >>> tot_col_v2(sum, test_file, 5, nhr=2)
    20.0
    """
    return fn_col(sum, f, col, delim, nhr)


#____________________________________________________________________________

# Q2. Design a function to determine on how many days the value in a given
# column meets some given boolean condition.  So, for example, we might
# want to know on how many days the average temperature was below 0C or
# on how many days the total rainfall was between 5 and 10mm.

def num_days_col_is(f, col, bfn, delim=None, nhr=0):
    """
    file, int, (float -> bool), str, int -> int

    Produces number of days the value v in a specified column of file f is
    such that bfn(v) is true

    >>> test_file = StringIO('row1\\n0,1,2,3\\n4,5,-6,7\\n8,9,-10,11')
    >>> num_days_col_is(test_file, 2, lambda x: x<0, ',', nhr = 1)
    2
    >>> test_file = StringIO('row1\\n0,1,8,3\\n4,5,6,7\\n8,9,10,11')
    >>> num_days_col_is(test_file, 2, lambda x: 5<x<10, ',', nhr = 1)
    2
    """
    skip_rows(f, nhr)
    
    acc = 0
    
    for line in f: 
        if line.strip() != '':
            if bfn(item_in_col(line,col,delim)):
                acc = acc + 1
                
    return acc
        
        

# Q2b. Make calls to your function from the Python Shell to determine:
# - the number of days during the year that the max temperature was below 10C
# - the number of days during the year that the rainfall was at least 5mm
#   but less than 10mm

# Make a note of the calls that you made to your function and the result
# produced so that they can be checked by your TA:


#==============================================================================
# >>> with open('yvr_2011.csv', 'U') as f:
# ...     num_days_col_is(f, 5, lambda x: x<10, ',', 24)
# ... 
# 131
# 
# >>> with open('yvr_2011.csv', 'U') as f:
# ...     num_days_col_is(f, 15, lambda x: 5<=x<10, ',', 24)    
#==============================================================================
... 
#37

#____________________________________________________________________________

# Q3. Design a function that uses the matplotlib library to generate a graph 
# of the mean daily temperature for each day of the year.  Use the
# number of days since the start of the year as the independent variable.
# Label both axes and give your chart the title:
#    Mean Daily Temperature: <name of file f>
# So, if f is the file named 'yvr_2011.csv' then the title of your chart will
# be:
#    Mean Daily Temperature: yvr_2011.csv
#
# Save your chart as a .png file named yvr_2011.png
#
# Hint: you will need to skim through the documentation for matplotlib.pyplot
# http://matplotlib.sourceforge.net/api/pyplot_api.html
# to find functions that allow you to specify labels, set tick marks and
# save a plot to a file.

def plot_mdt(f, delim=None, nhr=0):
    """
    file, str, int -> NoneType

    Effect: generates plot of mean temperature against day of year for data
    in file f

    <Can't test this one.>
    """
    lomdt= file_2_mdt(f, delim, nhr)    
    pyplot.plot(y=lomdt, 'r^', linestyle='-', linewidth=1)
    pyplot.show()
    
    def file_2_mdt(f, delim, nhr):
       skip_rows(f, nhr)
       return [[float(num) for num in line.split(delim)] for line in f if line.strip() != '']
    
            


# Q3b. Make a call to your function from the Python Shell and verify that
#     the required file has been produced and contains the expected plot.

# Make a note of the call that you make to your function so that it
# can be checked by your TA:





# Check that the file was created containing the expected data.



#____________________________________________________________________________

# Q4. Design a function that walks the directory EnvCanData and produces
# a plot of the mean daily temperature for every .csv file found in that
# directory or any of its subdirectories.  The plot must be saved to
# a .png file having the same name as the .csv file.  Be on the lookout for
# operations on data of arbitrary size and design helpers to process this
# data.  Note that all the .csv files have the same format as
# yvr_2011.csv.
#
# Hint: you will need to make a call to pyplt.cla() to clear one plot
# before generating the next.  Otherwise, successive plots will be added
# to the same set of axes.

def plot_mdt_dir(rdir, delim=None, nhr=0):
    """
    str, str, int -> NoneType

    Effect: generates plot of mean temperature against day of year for data
    in each .csv file found in rdir or any of its subdirectories.

    <Can't test this one.>
    """
    return None




#Q4b. Make a call to your function from the Python Shell and verify
#     that the required files containing the plots have been produced.

# Make a note of the call that you make to your function so that it
# can be checked by your TA:








#____________________________________________________________________________

# Make sure doctests run whenever this module is run.

if __name__=='__main__':
    import doctest
    EPS = 1.0e-9
    print(doctest.testmod(verbose=False))
