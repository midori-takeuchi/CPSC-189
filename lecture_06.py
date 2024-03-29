# CPSC 189 Lecture 06

from io import StringIO
import os
import math
import matplotlib.pyplot as pyplot


# Be sure to download rawData.zip from the course web page
# and unzip it into the same directory as this Python source file.
# You will also need to download observed.txt and add it to the
# same directory.

# Design a function that computes the average of data stored in a file
# where each number is not necessarily on a line of its own but numbers
# on the same line are separated by a specified delimiter. We assume
# that our file has a number of header rows that we need to skip
# over...

def average_file(f, delim=None, num_header_rows=0):
    """
    file, str, int -> float

    Produces the average of data in file f
    Requires: data is separated by string delim, there are num_header_rows
    at top of file to be ignored

    >>> test_file = StringIO('***\\nHeader\\n***\\n1, 2, 3\\n' \
                                      '4\\n5, 6, 7\\n')
    >>> act = average_file(test_file, ',', 3)
    >>> exp = 4.0
    >>> abs(act - exp) < EPS * exp
    True
    """
    skip_rows(f, num_header_rows)

    return average_file_no_header(f, delim)


def skip_rows(f, num_header_rows):
    """
    file, int -> NoneType

    Effect: skips ahead num_header_rows rows in file f

    >>> test_file = StringIO('row1\\nrow2\\nrow3\\nrow4\\n')
    >>> skip_rows(test_file, 3)
    >>> test_file.readline()
    'row4\\n'
    """
    for row in range(num_header_rows):
        f.readline()
 

def average_file_no_header(f, delim=None):
    """
    file, str -> Real

    Produces the average of data in file f
    Requires: reals are separated by delimiter, there is at least one real
    in file

    >>> test_file = StringIO('1 2 3\\n4\\n5 6 7\\n \\n')
    >>> act = average_file_no_header(test_file)    #<--- use default argument
    >>> exp = 4.0
    >>> abs(act - exp) < EPS * exp
    True

    >>> test_file = StringIO('1, 2, 3\\n4\\n5, 6, 7\\n \\n')
    >>> act = average_file_no_header(test_file, ',')
    >>> exp = 4.0
    >>> abs(act - exp) < EPS * exp
    True
    """
    total = 0.0
    count = 0

    for line in f:
        if line.strip() != '':
            data = line.split(delim)
            total = total + sum_data(data)
            count = count + len(data)

    return total / count


def sum_data(data):
    """
    (listof str) -> Real

    Produces the sum of the floats in the string data
    Requires: each string can be parsed as a float

    >>> act = sum_data(['1.5', '4.5', '3.5'])
    >>> exp = 9.5
    >>> abs(act - exp) < EPS * exp
    True
    """
    return sum([float(numstr) for numstr in data])




# Now suppose that we have a function that operates on a file (like
# average_file above) and that we want to apply that function to a 
# number of files contained in a folder on disk.  We assume that 
# there are an arbitrary number of files and that they are possibly 
# distributed through folders within folders...


# Problem 1: design a function that "walks" a directory structure and prints
# out data provided to us by the os.walk function...

def print_os_walk(rdir):
    """
    str -> NoneType

    Prints a walk of the OS file system rooted at rdir
    """
    for root, lodn, lofn in os.walk(rdir):
        print(root, lodn, lofn)


# Make sure you have the directory RawData in the same
# directory as this python source file.  Run the source file in a Python shell,
# change the working directory of the shell to the src directory of your
# Python project, then try the following in the Python shell:

# print_os_walk('RawData')

# What you see printed is the root (path to the directory we are currently
# visiting), lodn (list of sub-directory names for directory we are currently
# visiting) and lofn (list of file names in directory we are currently visiting).

# Open the folder RawData and compare what you see in the folder with
# what is printed on the screen.  Note that you may see some file names in lofn
# that you don't see when you open your file explorer window - these are hidden
# system files that are not normally shown to the user.



# Problem 2: design a function that computes the average of data in every .csv
# file in a directory tree and writes that average to another file in the
# same directory. So, for each .csv file f.csv, we will create a file
# f_avg.txt that contains the average of the data in f.csv

def average_file_dir(rdir, delim=None, num_header_rows=0):
    """
    str, str, int -> NoneType

    Computes the average of data stored in each file with a .csv extension
    in the directory rooted at rdir and saves result in another file.
    """
    for root, lodn, lofn in os.walk(rdir):
        average_file_lof(root, lofn, delim, num_header_rows)


def average_file_lof(root, lofn, delim=None, num_header_rows=0):
    """
    str, (listof str), str, int -> NoneType

    Computes the average of data stored in each file with a .csv extension
    in the list of files lofn and saves result in another file.
    """
    for fn in lofn:
        name, ext = os.path.splitext(fn)
        if ext == '.csv':
            with open(os.path.join(root, fn), 'U') as inf:
                avg = average_file(inf, delim, num_header_rows)
            with open(os.path.join(root, name + '_avg.txt'), 'w') as outf:
                outf.write('Average: ' + str(avg))


# In the Python shell, test your function...

# average_file_dir('RawData', ',', 3)


# If you now explore the RawData directory, you'll see that for each .csv file
# f.csv a new file has been created named f_avg.txt that contains the average
# of the data in f.



# The matplotlib library (http://matplotlib.org/)

# We've seen the following functions in an earlier lecture...

# This function produces the position of a particle given a time t
# according to the formula: p = 100 e^(-t/10) sin(2 * PI * t)

def position(t):
    """
    Real -> Real

    Produces the position of a particle at time t

    >>> exp = 0.0
    >>> act = position(0.0)
    >>> abs(exp - act) < EPS
    True
    >>> exp = 0.0
    >>> act = position(1.0)
    >>> abs(exp - act) < EPS
    True
    >>> exp = 97.5309912028333
    >>> act = position(0.25)
    >>> abs(exp - act) < EPS * exp
    True
    """
    return 100.0 * math.exp(-t / 10.0) * math.sin(2 * math.pi * t)


#The following function consumes a list of times and produces a list
#of positions.

def lot_2_lopn(lot):
    """
    (listof Real) -> (listof Real)

    Produces a list of positions of a particle at the times in lot

    >>> exp = [0.0, 0.0, 0.0]
    >>> act = lot_2_lopn([0.0, 0.5, 1.0])
    >>> all([abs(e - a) < EPS for (e, a) in zip(exp, act)])
    True

    >>> exp = [position(0.25), position(0.75), position(1.25)]
    >>> act = lot_2_lopn([0.25, 0.75, 1.25])
    >>> all([abs(e - a) < EPS * abs(e) for (e, a) in zip(exp, act)])
    True
    """
    return [position(t) for t in lot]


# Problem 3: Now suppose we want to design a function that consumes a 
# list of times and generates a 2D plot of position against time for 
# each time in the given list of times.  We call this function 
# plot_posn_theoretical as the data is generated from a theoretical 
# model.

def plot_posn_theoretical(lot):
    """
    (listof Real) -> NoneType

    Effects: generates a plot of position (defined by fn posn)
    against time for times in lot
    """
    loposns = lot_2_lopn(lot)
    pyplot.plot(lot, loposns, 'r^', linestyle='-', linewidth=1)
    pyplot.show()
    

# Note that the implementation above could be replaced with the following:

#    loposns = lot_2_lopn(lot)
#    l = (lot, loposns, 'r*')                 # the args as a tuple
#    d = dict(linestyle='-', linewidth=1)     # the kwargs as a dictionary
#    pyplot.plot(*l, **d)                     
#    pyplot.show()

# Test your function by calling it from a Python shell:
#
# plot_posn_theoretical([t/100 for t in range(100)])
#
# NOTE: the window that shows the plot might open up behind Eclipse so,
# if you don't see the plot, minimize your Eclipse window.



# Problem 4: Now suppose we have some empirical data for the position 
# of a particle at time t and that this data is stored in a file 
# "observed.txt". We call this function plot_posn_empirical as it 
# plots empirical data.

def plot_posn_empirical(f, delim=None):
    """
    file, str -> NoneType
    
    Effects: generates a plot of position against time for 
    data read from file f
    
    Requires: each row of file contains two Reals, the first a time
    in seconds, the second a position in metres, separated by delim.
    There are no empty lines in the file.
    """
    (lot, loposns) = file_2_lists(f, delim)
    pyplot.plot(lot, loposns, 'r^', linestyle='-', linewidth=1)
    pyplot.show()
    
    
def file_2_lists(f, delim=None):
    """
    file, str -> ((listof Real), (listof Real))
    
    Produces a tuple whose first element is a list of times 
    and whose second element is a list of positions read from
    file.
    
    Requires: each row of file contains two Reals, the first a time
    in seconds, the second a position in metres, separated by delim.
    There are no empty lines in the file.
    
    >>> test_file = StringIO('1.0, 1.0\\n1.5, 2.0\\n2.0, 3.0\\n')
    >>> act = file_2_lists(test_file, ',')
    >>> exp = ([1.0, 1.5, 2.0], [1.0, 2.0, 3.0])
    >>> act == exp
    True
    """
    lot = []
    loposns = []
    
    for line in f:
        (time, posn) = parse_line(line, delim)
        lot.append(time)
        loposns.append(posn)
        
    return (lot, loposns)

        
def parse_line(line, delim=None):
    """
    str -> (Real, Real)
    
    Parses the line to produce a tuple containing a time and position
    
    Requires: time and position are separated by delim    
    
    >>> act = parse_line('1.0 2.5')
    >>> exp = (1.0, 2.5)
    >>> act == exp
    True
    
    >>> act = parse_line('1.0, 2.5', ',')
    >>> exp = (1.0, 2.5)
    >>> act == exp
    True
    """
    data = line.split(delim)
    time = float(data[0])
    posn = float(data[1])
    return (time, posn)
    

# Test your function by calling it from the Python shell
# (again, it's important that the current working directory
# of the shell be set to the src folder in your Python
# project):

#with open('observed.txt', 'U') as inf:
#    plot_posn_empirical(inf, ',')
    
    

#_____________________________________
    

# Make sure doctest run when file is run but not imported

if __name__=='__main__':
    import doctest
    EPS = 1.0e-6
    print(doctest.testmod(verbose=False))