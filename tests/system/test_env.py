import os

import pygemstones.system.env as e


# -----------------------------------------------------------------------------
def test_remove_var():
    var_name = "MY_VAR"

    os.environ[var_name] = "test"
    assert os.environ[var_name] is not None

    e.remove_var(var_name)
    assert (var_name in os.environ) == False
