def truncate(file):
    """
        Truncate a file so it's empty on the next script run.
    """
    f = open(file, 'w') 
    f.close()
