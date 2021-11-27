import pygemstones.type.list as l


# -----------------------------------------------------------------------------
def test_filter_list():
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    new_values = l.filter_list(values, [7])

    assert len(new_values) == 9


# -----------------------------------------------------------------------------
def test_list_has_value():
    values = ["A", "B", "C"]

    assert l.list_has_value(values, "A")
    assert l.list_has_value(values, "Z") == False
    assert l.list_has_value(None, "A") == False
    assert l.list_has_value(values, None) == False


# -----------------------------------------------------------------------------
def test_get_arg_list_value():
    args = ["--param1=myvalue", "--version=1.2.3"]

    assert l.get_arg_list_value(args, "--version") == "1.2.3"
    assert l.get_arg_list_value(args, "--xyz") == None
