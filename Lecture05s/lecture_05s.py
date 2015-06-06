#CPSC 189 Lecture 05 -- Starter File

from io import StringIO 

#1. Design a function that copies a text file to the screen

def print_2_scrn(f):
    """
    file -> NoneType

    Effect: print file f on the screen line-by-line
    """
    for line in f:
        print(line, end = '') 
   


#2. Design a function that copies one text file to another     

def copy_file(inf, outf):
    """
    file, file -> NoneType

    Copies contents of inf to outf
    """
    for line in inf:
        outf.write(line)
        


#3. Design a function to compute the average of reals stored in a file.  We
# assume that each real number is on a line of its own.

def average_file(f):
    """
    file -> float
    
    Produces the average of data in file f
    Requires: at most one real number per line;
              there is at least on real number in the file
              
    >>> test_file = StringIO('1\\n2\\n   \\n3\\n   \\n')
    >>> act = average_file(test_file)
    >>> exp = 2.0
    >>> abs(act-exp) < EPS * exp
    True
    """
    total = 0.0
    count = 0
    
    for line in f: 
        if line.strip() != '':
            total = total + float(line)
            count = count + 1
            
    return total / count





#4. Design a function to compute the number of reals in a file
# that are below a given threshold value.  Again assume that each real
# number is on a line of its own.







#5. Design a function that computes the average of data stored in a file
# where each number is not necessarily on a line of its own but numbers
# on the same line are separated by a specified delimiter.  Note the use
# of a default argument below.  If an argument has a default value
# specified, the corresponding parameter does not have to be passed
# when the function is called.  If the parameter is not explicitly passed,
# the default value is assumed.  Arguments with default values must be listed
# after those that do not have default values.

def average_file_no_header(f, delim=None):
    """
    file, str -> float
    
    Produces average of data in file f
    Requires: reals are separated by delim string, 
    there is at least one real in the file
    
    >>> test_file = StringIO('1 2 3\\n4\\n5 6 7\\n  \\n')
    >>> act = average_file_no_header(test_file)
    >>> exp = 4.0
    >>> abs(act-exp) < EPS * exp
    True
    
    >>> test_file = StringIO('1, 2, 3\\n4\\n5, 6, 7\\n  \\n')
    >>> act = average_file_no_header(test_file, ',')
    >>> exp = 4.0
    >>> abs(act-exp) < EPS * exp
    True
    
    """
    total = 0.0
    count = 0
    
    for line in f:
        if line.strip() != '':
            data = line.split(delim)
            total = total + sum_data(data)
            count = count + len(data) #counting number of items on line
            
    return total / count
    
    
def sum_data(data):
    """
    (listof str) -> float
    
    Produces the sum of the floats in the string data
    Requires: each string can be parsed as a float
    
    >>> act = sum_data(['1.5', '4.5', '3.5'])
    >>> exp = 9.5
    >>> abs(act-exp) < EPS * exp
    True
    """
    return sum(float(numstr) for numstr in data)
    


#6. Now suppose that our file has a number of header rows that we need to skip
# over...

def average_file_header(f, delim=None, num_header_rows=0):
    """
    file, str, int -> float
    
    Produces the average of data in file f
    Requires: data is separated by string delim, there are num_header_rows
    at top of file to be ignored
    
    >>> test_file = StringIO('***\\nHeader\\n****\\n1, 2, 3\\n')
    >>> act = average_file_header(test_file, ',', 3)
    >>> exp = 2.0
    >>> abs(act-exp) < EPS * exp
    True
    """
    skip_rows(f, num_header_rows)
    
    return average_file_no_header(f, delim)
    

def skip_rows(f, num_header_rows):
    """ 
    file, int -> NoneType
    
    Effect: skips over num_header_rows in file f
    
    >>> test_file = StringIO('***\\nHeader\\n****\\n1, 2, 3\\n')
    >>> skip_rows(test_file, 3)
    >>> test_file.readline()
    '1, 2, 3\\n'
    >>>
    """
    for num in range(num_header_rows):
        f.readline()


# Make sure doctest run when file is run but not imported

if __name__=='__main__':
    import doctest
    EPS = 1.0e-9
    print(doctest.testmod(verbose=False))