import colorama

import pygemstones.system.settings as s


# -----------------------------------------------------------------------------
def init(params={}):
    """
    Initialize PyGemstones and it internal modules.

    After initialize it set pygemstones.system.settings.initialized as true

    Arguments:
        params : dict

    Returns:
        None
    """

    if s.initialized:
        return

    colorama.init()

    s.initialized = True
