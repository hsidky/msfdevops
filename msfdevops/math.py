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
    
    ret = float(sum(num_list))/len(num_list)
    return ret