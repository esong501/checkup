def index_to_col(n):
    """ takes an integer n and translates it to an Excel col identifier.
        ord('A') returns 65 in Python3.
        Cells in Excel start at 1 and so for consistency's sake,
        we will keep our indices starting at 1.
    """
    assert (n > 0 and n % 1 == 0), 'argument to index_to_col must be a positive integer'
    col = ""
    while n // 26 > 0:
        if n == 26:
            break
        elif n % 26 == 0:
            col = chr((n % 26) + 90) + col
            n = (n // 26) - 1
        else:
            col = chr((n % 26) + 64) + col
            n //= 26
    if n % 26 == 0:
        col = chr((n % 26) + 90) + col
    else:
        col = chr((n % 26) + 64) + col
    return col
    
def col_to_index(col):
    """ takes a string representing an Excel column identifier and
        translates it to a numberic index (starting at 1)
    """
    n = 0
    for i in range(len(col)):
        n += (26**i)*(ord(col[i]) - 64)
    return n

def get_int(cell):
    """ takes a worksheet cell and returns the associated integer value
    """
    return int(cell.value)