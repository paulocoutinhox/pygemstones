import sys

# log foreground colors
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
PURPLE = "\033[95m"
LIGHT_PURPLE = "\033[94m"
GRAY = "\033[90m"
LIGHT_GRAY = "\033[97m"

# log background colors
BG_BLACK = "\033[40m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"

# log styles
BOLD = "\033[1m"
RESET = "\033[0m"

# characters
BULLET = "•"


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

    print("{0}[ERROR]{1} {2}".format(RED, RESET, msg))

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

    print("{0}[WARN]{1} {2}".format(YELLOW, RESET, msg))


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

    print("{0}[FATAL]{1} {2}".format(RED, RESET, msg))

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

    print("{0}[INFO]{1} {2}".format(CYAN, RESET, msg))


# -----------------------------------------------------------------------------
def s(msg):
    """
    Show success message.

    Arguments:
        msg : str

    Returns:
        None
    """

    print("{0}[SUCCESS]{1} {2}".format(GREEN, RESET, msg))


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
    Show a simple message.

    A formatted with foreground color, background color and styles can be used in msg parameter.

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

    print("{0}[OK]{1} {2}".format(GREEN, RESET, msg))


# -----------------------------------------------------------------------------
def failed(msg):
    """
    Show failed message.

    Arguments:
        msg : str

    Returns:
        None
    """

    print("{0}[FAILED]{1} {2}".format(RED, RESET, msg))


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

    print("{0}{1}{2}".format(color, msg, RESET))


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

    print("{0}{1}{2}{3} {4}".format(prefix, color, BULLET, RESET, msg))


# -----------------------------------------------------------------------------
def bold(msg, color=None):
    """
    Show bold message with optional color parameter.

    Arguments:
        msg : str

        color : str

    Returns:
        None
    """

    if color:
        print("{0}{1}{2}{3}".format(BOLD, color, msg, RESET))
    else:
        print("{0}{1}{2}".format(BOLD, msg, RESET))
