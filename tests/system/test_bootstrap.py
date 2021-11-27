import pygemstones.system.bootstrap as b
import pygemstones.system.settings as s
from pygemstones import __version__


# -----------------------------------------------------------------------------
def test_init():
    assert s.initialized == False
    b.init()
    assert s.initialized == True


# -----------------------------------------------------------------------------
def test_reinit():
    b.init()
    b.init()
    assert s.initialized == True
