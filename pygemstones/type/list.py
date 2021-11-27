# -----------------------------------------------------------------------------
def filter_list(values, excludes):
    """
    Filter a list of values excluding all elements from excludes parameters and return the new list.

    Arguments:
        values : list

        excludes : list

    Returns:
        list
    """

    return list(x for x in values if x not in excludes)


# -----------------------------------------------------------------------------
def list_has_value(values, value):
    """
    Check if a list of values has a specific value validating if both are valid.

    Arguments:
        values : list

        value : any

    Returns:
        bool
    """

    if not values or not value:
        return False

    if value in values:
        return True

    return False


# -----------------------------------------------------------------------------
def get_arg_list_value(arg_values, key):
    """
    Check and return an argument value by key.

    Arguments:
        arg_values : list

        key : str

    Returns:
        str
    """

    for item in arg_values:
        if item and item.startswith("{0}=".format(key)):
            return item[(len(key) + 1) :]

    return None
