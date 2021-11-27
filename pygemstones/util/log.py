import sys

# log colors
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[1;36m"
PURPLE = "\033[95m"
BOLD = "\033[1m"
ENDC = "\033[0m"


# -----------------------------------------------------------------------------
def e(msg, fatal=True):
    """
    Show error message with a system exit as optional parameter.

    Arguments:
        msg : str

        fatal : bool

    Returns:
        None
    """

    print("{0}[ERROR]{1} {2}".format(RED, ENDC, msg))

    if fatal:
        sys.exit(10)


# -----------------------------------------------------------------------------
def w(msg):
    """
    Show warning message.

    Arguments:
        msg : str

    Returns:
        None
    """

    print("{0}[WARN]{1} {2}".format(YELLOW, ENDC, msg))


# -----------------------------------------------------------------------------
def f(msg="", fatal=True):
    """
    Show fatal error message with a system exit as optional parameter.

    Arguments:
        msg : str

        fatal : bool

    Returns:
        None
    """

    print("{0}[FATAL]{1} {2}".format(RED, ENDC, msg))

    if fatal:
        sys.exit(10)


# -----------------------------------------------------------------------------
def i(msg):
    """
    Show information message.

    Arguments:
        msg : str

    Returns:
        None
    """

    print("{0}[INFO]{1} {2}".format(BLUE, ENDC, msg))


# -----------------------------------------------------------------------------
def s(msg):
    """
    Show success message.

    Arguments:
        msg : str

    Returns:
        None
    """

    print("{0}[SUCCESS]{1} {2}".format(GREEN, ENDC, msg))


# -----------------------------------------------------------------------------
def d(msg):
    """
    Show debug message.

    Arguments:
        msg : str

    Returns:
        None
    """

    print("[DEBUG] {0}".format(msg))


# -----------------------------------------------------------------------------
def m(msg=""):
    """
    Show a clean message.

    Arguments:
        msg : str

    Returns:
        None
    """

    print(msg)


# -----------------------------------------------------------------------------
def ok(msg=""):
    """
    Show OK message with optional message appended.

    Arguments:
        msg : str

    Returns:
        None
    """

    print("{0}[OK]{1} {2}".format(GREEN, ENDC, msg))


# -----------------------------------------------------------------------------
def failed(msg):
    """
    Show failed message.

    Arguments:
        msg : str

    Returns:
        None
    """

    print("{0}[FAILED]{1} {2}".format(RED, ENDC, msg))


# -----------------------------------------------------------------------------
def colored(msg, color):
    """
    Show a colored message.

    Arguments:
        msg : str

        color : str

    Returns:
        None
    """

    print("{0}{1}{2}".format(color, msg, ENDC))


# -----------------------------------------------------------------------------
def bullet(msg, color, prefix="  "):
    """
    Show a bullet message with color and prefix.

    Arguments:
        msg : str

        color : str

        prefix : str

    Returns:
        None
    """

    print("{0}{1}•{2} {3}".format(prefix, color, ENDC, msg))


# -----------------------------------------------------------------------------
def bold(msg, color=None):
    """
    Show bol message with optional color parameter.

    Arguments:
        msg : str

        color : str

    Returns:
        None
    """

    if color:
        print("{0}{1}{2}{3}".format(BOLD, color, msg, ENDC))
    else:
        print("{0}{1}{2}".format(BOLD, msg, ENDC))
