# CPSC 189, Lab 03 - File I/O

from io import StringIO

# Global assumptions: files have expected number of header rows and
# data in file is separated by specified delimiter.  There is at least one
# row of data in the file.  There could be rows that contain only
# whitespace (spaces or tabs or newlines).

# The following function from lecture is provided for use in this lab:

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

# In the questions that follow, we assume that we are working
# with Environment Canada data in the file yvr_2011.csv (or a similarly
# formatted file) which we assume is in the same directory as this Python
# source file.

#____________________________________________________________________________

# Q0. The files that we are working with in this lab are formatted in
# such a way that there are multiple data points on each line of the file.
# In many of the exercises that follow, we will want to extract a
# data point from a particular column.  We will therefore begin by
# designing a function to perform this task.

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

# Q1. Design a function that can compute the average of data from a 
# specified column in a file (assume the column contains data of 
# type float).

def avg_col(f, col, delim=None, nhr=0):
    """
    file, int, str, int -> float

    Produces average of data stored in column col of file f

    Requires: file has nhr header rows of data; data is separated by delim

    >>> test_file = StringIO('***\\nHeader\\n****\\n1, 2, 3\\n1, 2, 3\\n')
    >>> act = avg_col(test_file, 2, ',', 3)
    >>> exp = 3.0
    >>> abs(act-exp) < EPS * exp
    True
    
    >>> test_file = StringIO('***\\nHeader\\n****\\n1 2 3\\n1 2 3\\n  \\n')
    >>> act = avg_col(test_file, 2, nhr=3)
    >>> exp = 3.0
    >>> abs(act-exp) < EPS * exp
    True
    
    """
    skip_rows(f, nhr)
    
    total_acc = 0
    count_acc = 0
    
    for line in f: 
        if line.strip() != '':
            total_acc = total_acc + item_in_col(line, col, delim)
            count_acc = count_acc + 1
            
    return total_acc / count_acc
    





# Q1b. Make calls to your function from the Python Shell to determine:
# - the average maximum temperature (C) for data in the file yvr_2011.csv
# - the average total rain (mm) for data in the file yvr_2011.csv

# Make a note of the calls made to your function and the values produced
# so that they can be checked by your TA:


#==============================================================================
# >>> with open('yvr_2011.csv', 'U') as f:
# ...     avg_col(f, 5, ',', 24)
# ... 
# 13.324383561643828
# 
# >>> with open('yvr_2011.csv', 'U') as f:
# ...     avg_col(f, 15, ',', 24)
# ... 
# 2.8695890410958906
#==============================================================================




#____________________________________________________________________________

# Q2. Design a function that can compute the maximum of data from a 
# specified column in a file (assume the column contains data of 
# type float).  Hint: look at the documentation for Python's built-in
# functions to find a useful helper function!

def max_col(f, col, delim=None, nhr=0):
    """
    file, int, str, int -> float

    Produces the maximum value of data stored in given column of file f
    
    Requires: file has nhr header rows of data; data is separated by delim

    >>> test_file = StringIO('***\\nHeader\\n****\\n1, 2, 3\\n3, 1, 5\\n')
    >>> act = max_col(test_file, 2, ',', 3)
    >>> exp = 5.0
    >>> abs(act-exp) < EPS * exp
    True
    """
    skip_rows(f, nhr)
    
    acc = []
    for line in f: 
        if line.strip() != '':
            acc = acc + [item_in_col(line, col, delim)]
        
    return max(acc)
        






# Q2b. Now make a call to your function from the Python Shell to determine
# the largest maximum temperature over the year.

# Make a note of the call you made to your function and the value produced
# so that they can be checked by your TA:


#==============================================================================
# >>> with open('yvr_2011.csv', 'U') as f:
# ...     max_col(f, 5, ',', 24)
# ... 
#==============================================================================
#27.4

#____________________________________________________________________________

# Q3. Design a function that can compute the sum of data from a 
# specified column in a file (assume the column contains data of 
# type float).  Hint: look at the documentation for Python's built-in
# functions to find a useful helper function!

def tot_col(f, col, delim=None, nhr=0):
    """
    file, int, str, int -> Real

    Produces the sum of data stored in given column of file f

    >>> test_file = StringIO('row1\\n row2\\n 0, 1, 2, 3, 4, 5, 6, 7\\n  \\n')
    >>> act = tot_col(test_file, 5, ',', 2)
    >>> exp = 5.0
    >>> abs(act-exp) < EPS * exp
    True

    >>> test_file = StringIO('row1\\n row2\\n 0 1 2 3 4 5 6 7\\n' \
                             '  \\n10 11 12 13 14 15 16 17\\n')
    >>> act = tot_col(test_file, 5, nhr=2)
    >>> exp = 20.0
    >>> abs(act-exp) < EPS * exp
    True
    """
    skip_rows(f, nhr)
    
    total = 0
    
    for line in f: 
        if line.strip() != '':  
            total = total + item_in_col(line, col, delim)
    return total 
 



# Q3b. Now make a call to your function from the Python Shell to determine
# the sum of the total daily rain fall over the year.

# Make a note of the call you made to your function and the value produced
# so that they can be checked by your TA:

#==============================================================================
# >>> with open('yvr_2011.csv', 'U') as f:
# ...     tot_col(f, 15, ',', 24)
# ... 
# 1047.4
#==============================================================================





#____________________________________________________________________________

# Aside: note the similarity in the design of the functions in Q2 and Q3.
# We'll look at a way to avoid this redundancy in class next week.
# Remember function abstraction?



#____________________________________________________________________________

# Q4. Design a function that produces a file that contains only the data
# stored in a specified column of the Environment Canada csv file.  The data
# must be written one value per row in the output file with no additional
# characters.

# Note: the tests have been provided for you but take time to ensure that
# you understand how they work.  How to design tests for functions that write
# data to files is covered in the readings.

#===============================================================================
# def write_col(inf, outf, col, delim=None, nhr=0):
#     """
#     file, file, int, str, int -> NoneType
# 
#     Effect: writes to file outf data from column col of inf
#     All header rows from inf are ignored and not written to outf.
#     
#     Requires: file has nhr header rows of data; data is separated by delim
# 
#     >>> file_data = 'H1\\nH2\\nH3\\n0.0 1.0 2.0 3.0\\n   \\n'
#     >>> test_infile = StringIO(file_data)
#     >>> test_outfile = StringIO()
#     >>> write_col(test_infile, test_outfile, 2, nhr=3)
#     >>> test_outfile.getvalue()
#     '2.0\\n'
# 
#     >>> file_data = 'H1\\nH2\\nH3\\n0.0 1.0 2.0 3.0\\n'  \
#                                    '   \\n4.0 5.0 6.0 7.0\\n  \\n'
#     >>> test_infile = StringIO(file_data)
#     >>> test_outfile = StringIO()
#     >>> write_col(test_infile, test_outfile, 2, nhr=3)
#     >>> test_outfile.getvalue()
#     '2.0\\n6.0\\n'
#     """
#     return None   #stub
#===============================================================================







# Q4b) Make a call to your function from the Python Shell so that data
# from column 5 in yvr_2011.csv is written to the file yvr_2011_5.txt.

# Make a note of the call that you make to your function so that it
# can be checked by your TA:





# Check that the file was created containing the expected data.




#____________________________________________________________________________

# Q5. Design a function that consumes a file that contains a table
# of numbers with at least one row of data and at least one number per row.  

# Your function must produce a list of all the numbers in the file
# in the order in which they appear in the file, reading left to right
# and top-down.  Study the provided tests carefully before continuing. 
#
# Your solution must make use of a list comprehension. However, you may want 
# to start by designing a solution using a loop and then refactoring the code 
# to use a list comprehension.

#===============================================================================
# def file_to_lon(f, delim=None, nhr=0):
#     """
#     file, str, int -> (listof Real)
#     
#     Produces a list of the numbers read from f
#     
#     >>> file_data = 'H1\\nH2\\nH3\\n0.0 1.0 2.0 3.0\\n'  \
#                                    '   \\n4.0 5.0 6.0 7.0\\n  \\n'
#     >>> test_file = StringIO(file_data)
#     >>> act = file_to_lon(test_file, nhr=3)
#     >>> exp = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
#     >>> act == exp
#     True
#     
#     >>> file_data = 'H1\\nH2\\nH3\\n0.0, 1.0, 2.0\\n'  \
#                                    '   \\n3.0, 4.0, 5.0\\n  \\n'
#     >>> test_file = StringIO(file_data)
#     >>> act = file_to_lon(test_file, ',', 3)
#     >>> exp = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
#     >>> act == exp
#     True
#     """
#     return []   #stub
#===============================================================================

# Q5b) Make a call to your function from the Python Shell and produce a list of
# the numbers found in the file heightData.txt

# Make a note of the call that you make to your function so that it
# can be checked by your TA:



# Check that the list printed on the console contains the expected data.





#____________________________________________________________________________
# Q6. Design a function that consumes a file that contains a table
# of numbers with at least one row of data and at least one number per row.   

# Your function must produce a list of lists of numbers.  Each list within
# the list of list of numbers must contain the numbers found on a single
# row of the file, in the order in which they appear on that row. Study
# the provided tests carefully before continuing. 
#
# Your solution must make use of a list comprehension. However, you may want 
# to start by designing a solution using a loop and then refactoring the code 
# to use a list comprehension.

#===============================================================================
# def file_to_lolon(f, delim=None, nhr=0):
#     """
#     file, str, int -> (listof (listof Real))
#     
#     Produces a list of list of numbers read from f, one list per row of numbers
#     
#     >>> file_data = 'H1\\nH2\\nH3\\n0.0 1.0 2.0 3.0\\n'  \
#                                    '   \\n4.0 5.0 6.0 7.0\\n  \\n'
#     >>> test_file = StringIO(file_data)
#     >>> act = file_to_lolon(test_file, nhr=3)
#     >>> exp = [[0.0, 1.0, 2.0, 3.0], [4.0, 5.0, 6.0, 7.0]]
#     >>> act == exp
#     True
#     
#     >>> file_data = 'H1\\nH2\\nH3\\n0.0, 1.0, 2.0\\n'  \
#                                    '   \\n3.0, 4.0, 5.0\\n  \\n'
#     >>> test_file = StringIO(file_data)
#     >>> act = file_to_lolon(test_file, ',', 3)
#     >>> exp = [[0.0, 1.0, 2.0], [3.0, 4.0, 5.0]]
#     >>> act == exp
#     True
#     """
#     return []   #stub
#===============================================================================

# Q6b) Make a call to your function from the Python Shell and produce a list of
# the numbers found in the file heightData.txt

# Make a note of the call that you make to your function so that it
# can be checked by your TA:



# Check that the list printed on the console contains the expected data.



#____________________________________________________________________________

# Q7a) Design a function that consumes a file containing only text and
# produces a tuple (#para, #sentence, #word) where #para is the number
# of paragraphs, #sentence is the number of sentences and #word is
# the number of words found in the document.

# We make the following simplifying assumptions:
# - we can determine the number of paragraphs by counting the number
#   of blank lines as there is always a single blank line between
#   paragraphs and a single blank line at the end of the file
# - we can determine the number of sentences by counting the number
#   of words that have a period at the end
# - words are separated by one or more spaces

# Data Definition

# TextAnalysis is (p_count=int, s_count=int, w_count=int)
# interp. the number of paragraphs, sentences and words in text

A1 = (10, 42, 225)
A2 = (1, 5, 56)

#def fn_for_text_analysis(t):
#    ...t[0] ...t[1] ...t[2]
    


#===============================================================================
# def analyze_text(f):
#     """
#     file -> TextAnalysis
#     
#     Produces a text analysis of the text in file f.
#     
#     >>> test_file = StringIO('')
#     >>> analyze_text(test_file)
#     (0, 0, 0)
#     
#     >>> test_file = StringIO('One para, one sentence, six words.\\n  \\n')
#     >>> analyze_text(test_file)
#     (1, 1, 6)
#     
#     >>> test_file = StringIO('One para, two sentence. Second sentence.\\n  \\n')
#     >>> analyze_text(test_file)
#     (1, 2, 6)
#     
#     >>> test_file = StringIO('First para, first sentence, 6 words.\\n \\n' \
#                              'Second para, second sentence, 6 words.\\n \\n' \
#                              'Third para, third sentence, 6 words.\\n \\n')
#     >>> analyze_text(test_file)
#     (3, 3, 18)
#     """
#     return (0, 0, 0)  #stub
#===============================================================================
    

# Q7b) Make a call to your analyze_text function and analyze the text in the file
# lorumIpsum.txt (this text is brought to you courtesy of http://www.lipsum.com/)


# Make a note of the call that you make to your function so that it
# can be checked by your TA:





#____________________________________________________________________________

# Make sure doctests run whenever this module is run.

if __name__=='__main__':
    import doctest
    EPS = 1.0e-6
    print(doctest.testmod(verbose=False))
