import pygemstones.system.platform as p


# -----------------------------------------------------------------------------
def test_windows():
    ret = p.is_windows()
    assert isinstance(ret, bool)


# -----------------------------------------------------------------------------
def test_linux():
    ret = p.is_linux()
    assert isinstance(ret, bool)


# -----------------------------------------------------------------------------
def test_macos():
    ret = p.is_macos()
    assert isinstance(ret, bool)
