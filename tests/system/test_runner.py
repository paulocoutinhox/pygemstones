import os
import sys

import pytest

import pygemstones.io.file as f
import pygemstones.system.platform as p
import pygemstones.system.runner as r


# -----------------------------------------------------------------------------
def test_run(capsys):
    if p.is_windows():
        r.run(["dir"])
    else:
        r.run(["ls"])

    captured = capsys.readouterr()
    assert captured.out == ""


# -----------------------------------------------------------------------------
def test_run_program_not_exists():
    with pytest.raises(SystemExit) as info:
        if p.is_windows():
            r.run(["dir", "---"])
        else:
            r.run(["ls", "---"])

    assert info.value.args[0] == 10


# -----------------------------------------------------------------------------
def test_run_shell(capsys):
    if p.is_windows():
        r.run(["dir"], shell=True)
    else:
        r.run(["ls"], shell=True)

    captured = capsys.readouterr()
    assert captured.out == ""


# -----------------------------------------------------------------------------
def test_run_as_shell_program_not_exists():
    with pytest.raises(SystemExit) as info:
        r.run(["xyz-program"], shell=True)

    assert info.value.args[0] == 10


# -----------------------------------------------------------------------------
def test_external(tmp_path):
    external_path = os.path.join(tmp_path, "external")
    f.create_dir(external_path)

    external_file_path = os.path.join(external_path, "mod1.py")

    file_content = "def run(args):\n  print(123)\n"
    f.set_file_content(external_file_path, file_content)

    r.run_external(
        external_path,
        "mod1",
        "run",
        [],
        show_error_log=True,
        show_log=True,
    )


# -----------------------------------------------------------------------------
def test_external_with_error(tmp_path):
    external_path = os.path.join(tmp_path, "external")
    f.create_dir(external_path)

    external_file_path = os.path.join(external_path, "mod1.py")

    file_content = "def run(args):\n  xyz()\n"
    f.set_file_content(external_file_path, file_content)

    with pytest.raises(SystemExit) as info:
        r.run_external(
            external_path,
            "mod1",
            "run",
            [],
            show_error_log=True,
            show_log=True,
        )

    assert info.value.args[0] == 10


# -----------------------------------------------------------------------------
def test_external_with_error_but_silent(tmp_path):
    external_path = os.path.join(tmp_path, "external")
    f.create_dir(external_path)

    external_file_path = os.path.join(external_path, "mod1.py")

    file_content = "def run(args):\n  xyz()\n"
    f.set_file_content(external_file_path, file_content)

    r.run_external(external_path, "mod1", "run", [])


# -----------------------------------------------------------------------------
def test_external_with_throw_error(tmp_path):
    external_path = os.path.join(tmp_path, "external")
    f.create_dir(external_path)

    external_file_path = os.path.join(external_path, "mod1.py")

    file_content = "def run(args):\n  xyz()\n"
    f.set_file_content(external_file_path, file_content)

    with pytest.raises(NameError) as info:
        r.run_external(
            external_path,
            "mod1",
            "run",
            [],
            show_error_log=True,
            show_log=True,
            throw_error=True,
        )

    assert info.value.args[0] == "name 'xyz' is not defined"


# -----------------------------------------------------------------------------
def test_run_silent(capfd):
    if p.is_windows():
        r.run(["dir"], silent=True)
    else:
        r.run(["ls"], silent=True)

    captured = capfd.readouterr()
    assert captured.out == ""


# -----------------------------------------------------------------------------
def test_run_silent_with_shell(capfd):
    if p.is_windows():
        r.run(["dir"], shell=True, silent=True)
    else:
        r.run(["ls"], shell=True, silent=True)

    captured = capfd.readouterr()
    assert captured.out == ""


# -----------------------------------------------------------------------------
def test_run_silent_error():
    with pytest.raises(FileNotFoundError) as info:
        r.run(["xyz-program"], silent=True)

    assert info.value.args[0] == 2


# -----------------------------------------------------------------------------
def test_run_silent_error_with_shell():
    with pytest.raises(SystemExit) as info:
        r.run(["xyz-program"], shell=True, silent=True)

    assert info.value.args[0] == 10


# -----------------------------------------------------------------------------
def test_run_with_default_environment(capfd):
    os.environ["PYGEMSTONES_VAR_1"] = "value1"

    r.run(["python3", "-c", "import os; print(os.environ['PYGEMSTONES_VAR_1'])"])

    captured = capfd.readouterr()
    assert captured.out.strip() == "value1"


# -----------------------------------------------------------------------------
def test_run_with_custom_environment(capfd):
    os.environ["PYGEMSTONES_VAR_1"] = "value1"

    custom_env = os.environ
    custom_env["PYGEMSTONES_VAR_1"] = "value2"

    r.run(
        ["python3", "-c", "import os; print(os.environ['PYGEMSTONES_VAR_1'])"],
        env=custom_env,
    )

    captured = capfd.readouterr()
    assert captured.out.strip() == "value2"
