import pygemstones.type.string as s


# -----------------------------------------------------------------------------
def test_bytes():
    file_size = 64
    readable = s.readable_file_size(file_size)
    assert readable == "64 b"


# -----------------------------------------------------------------------------
def test_bytes_float():
    file_size = 128.5
    readable = s.readable_file_size(file_size)
    assert readable == "128 b"


# -----------------------------------------------------------------------------
def test_bytes_large_amount():
    file_size = 123456789
    readable = s.readable_file_size(file_size)
    assert readable == "117 Mb"


# -----------------------------------------------------------------------------
def test_bytes_xlarge_amount():
    file_size = 123456789 * 123456789 * 123456789
    readable = s.readable_file_size(file_size)
    assert readable == "1 Yib"
