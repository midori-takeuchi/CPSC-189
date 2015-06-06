# Lecture 02
# Solutionss - Part 1

# Consider the following data definition:

#Non-Empty List Of X is one of:
    #- [X]
    #- [X] + Non-Empty List Of X
#interp. a non-empty list of items of type X

NELOX1 = [4]
NELOX2 = ['a', 'ab', 'abc']

#def fn_for_nelox(nelox):
    #if nelox[1:] == []:
        #return ...nelox[0]
    #else:
        #return ...nelox[0] ...nelox[1] ...fn_for_nelox(nelox[1:])


# This data definition is so commonly used that we'll use the following
# special syntax to represent it:

#(nelistof X)



#Problem 1: Design a function that consumes a non-empty list of reals and
#produces the largest real in that list.

#def max_nelon(nelon):
#    """
#    (listof Real) -> Real
# 
#    Produces the maximum of the entries in nelon
# 
#    >>> max_nelon([3])
#    3
# 
#    >>> max_nelon([1.0, 4.0, 3.0])
#    4.0
#     
#    >>> max_nelon([-2.1, -5.0, -8.5])
#    -2.1
#    """
# 
#    if nelon[1:] == []:
#        return nelon[0]
#    else:
#        if nelon[0] > max_nelon(nelon[1:]):
#            return nelon[0]
#        else:
#            return max_nelon(nelon[1:])


# Notice that on each call to max_nelon we potentially make *two* calls
# to max_nelon(nelon[1:]).  We can avoid this recomputation through
# the use of a local variable...

def max_nelon(nelon):
    """
    (listof Real) -> Real
 
    Produces the maximum of the entries in nelon
 
    >>> max_nelon([3])
    3
 
    >>> max_nelon([1.0, 4.0, 3.0])
    4.0
    """
 
    if nelon[1:] == []:
        return nelon[0]
    else:
        max_rest = max_nelon(nelon[1:])    # here's where we store the value
                                           # returned by the call
                                           # max_nelon(nelon[1:]) in a local
                                           # variable named max_rest
        if nelon[0] > max_rest:
            return nelon[0]
        else:
            return max_rest
        


#_________________________________________

#Make sure that tests run when this module is run.

if __name__=='__main__':
    import doctest
    EPS = 1.0e-6                         # for testing floats
    print(doctest.testmod(verbose=False))