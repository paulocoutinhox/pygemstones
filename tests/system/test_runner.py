import os

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
        r.run_as_shell(["dir"])
    else:
        r.run_as_shell(["ls"])

    captured = capsys.readouterr()
    assert captured.out == ""


# -----------------------------------------------------------------------------
def test_run_as_shell_program_not_exists():
    with pytest.raises(SystemExit) as info:
        r.run_as_shell(["xyz-program"])

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
