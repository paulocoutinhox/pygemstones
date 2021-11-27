import platform


# -----------------------------------------------------------------------------
def is_windows():
    """
    Check and return if running platform is Windows.

    Arguments:
        None

    Returns:
        bool
    """

    return any(platform.win32_ver())


# -----------------------------------------------------------------------------
def is_macos():
    """
    Check and return if running platform is macOS.

    Arguments:
        None

    Returns:
        bool
    """
    return platform.system().lower().startswith("darwin")


# -----------------------------------------------------------------------------
def is_linux():
    """
    Check and return if running platform is Linux.

    Arguments:
        None

    Returns:
        bool
    """

    return platform.system().lower().startswith("linux")
