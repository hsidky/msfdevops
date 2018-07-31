"""
Some miscellaneous math functions

More detailed descriptions here
"""

# imports go here
def mean(num_list):
    """
    Calculate the mean/average of a list of numbers 

    Parameters
    ----------
    num_list : list 
        The list to take the average of
    
    Returns
    -------
    ret: float 
        The mean of a list 
    
    Examples
    --------

    >>> mean([1, 2, 3, 4, 5])
    3.0
    """
    
    # Check that user passes list 
    if not isinstance(num_list, list): 
        raise TypeError("Input must be type list")
    
    # Check that the list has length 
    if len(num_list) == 0:
        raise ZeroDivisionError("Cannot calculate mean of empty list")

    try:
        ret = float(sum(num_list))/len(num_list)
    except TypeError:
        raise TypeError("Values of list must be int or float")
    return ret