import os


# -----------------------------------------------------------------------------
def remove_var(key):
    """
    Remove environment variable.

    Arguments:
        key: str

    Returns:
        None
    """

    os.environ.pop(key, None)
