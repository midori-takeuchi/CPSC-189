# CPSC 189: Lecture 02 Starter File

# Consider the following data definition:

#Non-Empty List Of X is one of:
    #- [x]
    #- [x] + Non-Empty List Of X
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



#Problem 1, Part 1: Design a function that consumes a non-empty list of reals 
#and produces the largest real in that list.






#Problem 1, Part 2
#==============================================================================
# def max_nelon(nelon):
#     """
#     (listof Real) -> Real
# 
#     Produces the maximum of the entries in nelon
# 
#     >>> max_nelon([3])
#     3
# 
#     >>> max_nelon([1.0, 4.0, 3.0])
#     4.0
#     """
# 
#     if nelon[1:] == []:
#         return nelon[0]
#     else:
#         max_rest = max_nelon(nelon[1:])    # here's where we store the value
#                                            # returned by the call
#                                            # max_nelon(nelon[1:]) in a local
#                                            # variable named max_rest
#         if nelon[0] > max_rest:
#             return nelon[0]
#         else:
#             return max_rest
#==============================================================================

#_________________________________________

#Problem 2: Design a function that consumes a list of integers
#and produces the sum of those integers that are positive.

#==============================================================================
# def sum_positive(loi):
#     """
#     (listof int) -> int
#     
#     Produces sum of the positive integers in loi
#     
#     >>> sum_positive([])
#     0
#     
#     >>> sum_positive([5,-4,3])
#     8
#     """
#     if loi == []:
#         return 0
#     else:
#         if loi[0] > 0:
#             return loi[0] + sum_positive(loi[1:])
#         else:
#             return sum_positive(loi[1:])
#==============================================================================



#_________________________________________


# Here's the process for redesigning the function so that the recursive
# call is in tail position (we use an accumulator to accomplish this):

#1. Nest the function definition inside an outer function of the same name.
#2. Rename outer parameter to loi0
#3. Move the documentation (including the doctests) to the outer function
#4. Add an accumulator as an extra parameter to the nested function definition
#5. Make a call to the nested function using ... in place of the accumulator
#6. Specify the type of the accumulator
#7. Write examples to illustrate how the accumulator works
#8. Write an invariant for the accumulator
#9. Replace the template with the function body ensuring that the invariant
#   is satisfied.

# Here's what you've got after completing steps 1 through 6:

def sum_positive(loi0):
    """
    (listof int) -> int

    Produces the sum of the positive integers in loi

    >>> sum_positive([])
    0

    >>> sum_positive([5, -4, 3])
    8
    """

    def sum_positive_acc(loi, acc):
        """
        Accumulator: acc is int

        Invariant: acc is the sum of the positive integers seen so far
        
        
        Examples:
        sum_positive_acc([5, -4, 3], 0)
        sum_positive_acc([-4, 3], 5)
        sum_positive_acc([3], 5)
        sum_positive_acc([], 8)
        """
        if loi == []:
            return sum_positive_acc
        else:
            if loi[0] > 0:
                return sum_positive_acc(loi[1:], loi[0] + acc)
            else:
                return sum_positive_acc(loi[1:], acc)

    return sum_positive_acc(loi0, 0)

            


#Problem 3: Complete steps 7, 8 and 9 by modifying the function provided above. 


#_________________________________________


#Problem 4: Redesign the following function so that the recursive call is in
#tail position.

#def reverse(los):
#    """
#    (listof str) -> (listof str)
#    
#    Produces a new list consisting of strings in los but in reverse order
#    
#    >>> reverse([])
#    []
#    
#    >>> reverse(['abc', 'def', 'ghi'])
#    ['ghi', 'def', 'abc']
#    """
#    if los == []:
#        return []
#    else:
#        return reverse(los[1:]) + [los[0]]

    
# Here's a start - fill in the missing parts of the design:
    
def reverse(los):
    """
    (listof str) -> (listof str)
    
    Produces a new list consisting of strings in los but in reverse order
    
    >>> reverse([])
    []
    
    >>> reverse(['abc', 'def', 'ghi'])
    ['ghi', 'def', 'abc']
    
    Accumulator: acc is listof str
    
    Invariant: acc is the list of str in reverse order seen so far 
    
    Example: reverse(['abc', 'def', 'ghi'])
    (['def', 'ghi'], ['abc'])
    (['ghi'], ['def', 'abc'])
    ([], ['ghi', 'def', 'abc'])
    """
    if los == []:
        return []
    else:
        return reverse(los[1:]) + [los[0]]


#_________________________________________


#Problem 5: Redesign the function given in Problem 1 so that the recursive call
#is in tail position.











#_________________________________________

#Make sure that tests run when this module is run.

if __name__=='__main__':
    import doctest
    EPS = 1.0e-6                         # for testing floats
    print(doctest.testmod(verbose=False))