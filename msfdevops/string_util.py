"""
Miscellaneous string functions
"""

# Imports go here


def title_string(s):
    """
    Converts a string to a title case 

    Title case means that the first character of
    every word is capitalized, otherwise lowercase
    
    Parameters
    ----------
    s : str
        The string to convert to title case

    Returns
    -------
    str 
        The input string in title case 

    Examples
    --------
    >>> title_string("this iS a StrING to be ConverTeD")
    'This Is A String To Be Converted'
    """

    # Check that input is string
    if not isinstance(s, str):
        raise TypeError("Input must be string")
    
    # Empty string 
    if len(s) == 0:
        raise IndexError("Cannot apply title function to empty string")

    ss = []
    for i, c in enumerate(s):
        nc = c
        if i == 0:
            nc = c.upper()
        elif s[i - 1] == " ":
            nc = c.upper()
        else:
            nc = c.lower()
        ss.append(nc)

    return "".join(ss)
