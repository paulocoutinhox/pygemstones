# -----------------------------------------------------------------------------
def readable_file_size(size, suffix="b"):
    """
    Return human readable file size.

    Arguments:
        size : int

        suffix : str

    Returns:
        str
    """

    unit_list = ["", "k", "M", "G", "T", "P", "E", "Z"]

    for unit in unit_list:
        if abs(size) < 1024:
            return "%d %s%s" % (size, unit, suffix)

        size /= 1024

    return "%d %s%s" % (size, "Yi", suffix)
