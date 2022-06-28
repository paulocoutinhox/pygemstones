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


# -----------------------------------------------------------------------------
def test_get_arg_list_values():
    args = ["--param1=myvalue1", "--param1=myvalue2"]
    values = l.get_arg_list_values(args, "--param1")
    assert len(values) == 2
    assert values[0] == "myvalue1"
    assert values[1] == "myvalue2"

    args = ["--param1=myvalue1", "--param2=myvalue2"]
    values = l.get_arg_list_values(args, "--param2")
    assert len(values) == 1
    assert values[0] == "myvalue2"

    args = ["--param1=myvalue1", "--param2=myvalue2"]
    values = l.get_arg_list_values(args, "--param3")
    assert len(values) == 0
