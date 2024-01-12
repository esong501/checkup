import os

def get_excel_files():
    """ within our current directory, we fetch all excel files (notated by suffix .xlsx)
        to later display to the user as a choice.
    """
    # Get the current directory
    curr_dir = os.getcwd()

    # List the files in the current directory
    files = os.listdir(curr_dir)

    xlfs = []
    for f in files:
        if f[-5:] == '.xlsx' and f[:2] != '~$':
            xlfs += [f]

    return xlfs
